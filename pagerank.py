import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    adjacent = corpus[page]
    probDist = {}
    if len(adjacent) == 0:
        for key in corpus.keys():
            probDist[key] = 1/len(corpus)

    for key in corpus.keys(): 
        if key not in adjacent:
            probDist[key] = (1-damping_factor)/len(corpus)
        else: 
            probDist[key] = (1-damping_factor)/len(corpus) + (damping_factor)/len(adjacent)
    return probDist

    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    samples = corpus.copy()
    for x in samples:
        samples[x] = 0
    sample = random.choice(list(corpus.keys()))
    for x in range(n):
        probs = []
        for i in transition_model(corpus, sample, damping_factor):
            probs.append(transition_model(corpus, sample, damping_factor)[i])
        sample = random.choices(list(corpus.keys()), probs, k=1)[0]
        samples[sample] += 1
    for x in samples:
        samples[x] = samples[x]/n
    return samples
    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    newRanks = {}
    oldRanks = {}
    for x in corpus:
        oldRanks[x] = 1/(len(corpus))
    change = 1
    while change > 0.001: 
        change = 0
        for i in corpus:
            condition2 = 0
            for j in corpus: 
                if len(corpus[j]) == 0:
                    condition2 += oldRanks[j]/len(corpus.keys())
                if i in corpus[j]:
                    condition2 += oldRanks[j]/len(corpus[j])
            condition2 *= damping_factor
            condition2 += (1-damping_factor)/len(corpus.keys())
            newRanks[i] = condition2
        for x in newRanks:
            if abs(newRanks[x] - oldRanks[x]) > change:
                change = abs(newRanks[x] - oldRanks[x])
        if change > 0.001:
            oldRanks = newRanks.copy()
    return oldRanks
    # raise NotImplementedError


if __name__ == "__main__":
    main()
