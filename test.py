from pix2text import Pix2Text

# File path to your image
img_fp = '1.png' # Replace with the path to your image

# Initialize the Pix2Text
p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))

# Recognize the content of the image
outs = p2t(img_fp, resized_shape=600) # You can also use `p2t.recognize(img_fp)` to get the same result

# Print the recognized text
print(outs)

# If you only need the recognized text and Latex representation, you can use the following code to merge all results
only_text = '\n'.join([out['text'] for out in outs])
print(only_text)
