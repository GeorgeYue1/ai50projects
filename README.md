I first tried the same exact number of layers and types of layers that was used in the source code of handwritten.py in the video lecture

# First Trial: 
* 2D Convolution layer with 32 filters and a 3x3 kernel
* MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 128 neurons and a dropout of 0.5

This model ended up have a loss of 3.5 and an accuracy of about 5.6%. It was clear that this model was performing very poorly, so I tried increasing the number of neurons in the hidden layer from 128 to 256. 

# Second Trial:
* 2D Convolution layer with 32 filters and a 3x3 kernel
* MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 256 neurons and a dropout of 0.5

This model had a loss of 3.5 and an accuracy of 5.55%. It seems like this model performed even worse somehow. I assumed that the number of neurons in the hidden wasn't the reason why this model was performing so poorly. I reverted the number of neurons from 256 to 128 and instead changed the number of filters in the 2D Convolution layer from 32 to 64. 

# Third Trial: 
* 2D Convolution layer with 64 filters and a 3x3 kernel
* MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 128 neurons and a dropout of 0.5

This model had a loss of 3.5 and an accuracy of 5.8%. This model performed slighty better than in the other two trials, but still performed very poorly overall. I reverted the number of filters back to 32 and tried a 4x4 kernel instead of 3x3. 

# Fourth Trial: 
* 2D Convolution layer with 32 filters and a 4x4 kernel
* MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 128 neurons and a dropout of 0.5

This model had a loss of 3.5 and an accuracy of 5.5%. It looks like the kernel size is not the reason for the low accuracy of the model. I reverted everything back to the original model and tried a dropout rate of 0.1

# Fifth Trial: 
* 2D Convolution layer with 32 filters and a 3x3 kernel
* MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 128 neurons and a dropout of 0.1

This model improved drastically compared to the previous trials. This model had a loss of 0.32 and an accuracy of 94.2%. It looks like the previous dropout rate of 0.5 was dropping out too many inputs for the model to perform well. I kept the dropout rate for the next model but changed the number of filters in the 2D Convolution layer from 32 to 64.

# Sixth Trial: 
* 2D Convolution layer with 64 filters and a 3x3 kernel
* MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 128 neurons and a dropout of 0.1

This model performed very similarly to the previous model. This model had a loss of 0.305 and an accuracy of 94.5%. I reverted the change and added a second 2D Convolution Layer with 32 filters and another MaxPooling layer with a 2x2 pool size.

# Seventh Trial: 
* 2, 2D Convolution layer with 64 filters and a 3x3 kernel
* 2, MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 128 neurons and a dropout of 0.1

This model again performed only slightly better with a loss of 0.25 and an accuracy of 94.9%. I will try to add one more Convolution layer and MaxPooling layer as well as increase the number of neurons in the Hidden Layer to 256. 

# Seventh Trial: 
* 3, 2D Convolution layer with 64 filters and a 3x3 kernel
* 3, MaxPooling with a 2x2 pool size
* 1 Dense Hidden Layer with 256 neurons and a dropout of 0.1

This model had a loss of 0.191 and an accuracy of 95.1%. The accuracy only increases by small increments from here. In conclusion, it looks like having more 2D Convolution layers, MaxPooling Layers, and more neurons in the Dense Hidden Layer helps improve accuracy, which was expected. Additionally, I found out that having a dropout rate that is too high prevents the model from performing well.