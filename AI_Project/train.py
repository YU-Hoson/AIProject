from models.ImageGener import StyleGAN
from models.TTS import tacotron

model = StyleGAN()
model2 = tacotron()

for epoch in epochs:
    for idx, data in enumerate(dataloader):

#학습 완료
