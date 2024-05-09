import os
import torch

x_t, uncond_embeddings = torch.load("/raid/lurenjie/MagicDance/TikTok-v4/nti/00001/xt_girl_512_512_50.pt"), torch.load("/raid/lurenjie/MagicDance/TikTok-v4/nti/00001/unc_girl_512_512_50.pt")
print(uncond_embeddings)
print(uncond_embeddings.shape)
