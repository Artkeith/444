```python
import random
from PIL import Image, ImageDraw

class ArtGenerator:
    def __init__(self):
        self.width = 800
        self.height = 800

    def generate_art(self):
        img = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(img)

        for _ in range(1000):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line((x1, y1, x2, y2), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        img.save('generated_art.png')

if __name__ == "__main__":
    art_gen = ArtGenerator()
    art_gen.generate_art()
```