import urllib.request

model_name = "512-depth-ema.ckpt"
model_name2 = "dpt_hybrid-midas-501f0c75.pt"
m_name = [model_name,model_name2]
num = 0
url = "https://huggingface.co/stabilityai/stable-diffusion-2-depth/resolve/main/"+model_name
url2 = "https://github.com/intel-isl/DPT/releases/download/1_0/"+model_name2
save_path = "midas_models/"+model_name
save_path2 = "midas_models/"+model_name2

def show_progress_bar(downloaded, total, chunk_size):
  progress = downloaded / total
  print(m_name[num] + " - " + str(round(progress, 2))+" %", end='\r')

# Download models
urllib.request.urlretrieve(url, save_path, reporthook=show_progress_bar)
print (m_name[num]+ " - done")
num+=1
urllib.request.urlretrieve(url2, save_path2, reporthook=show_progress_bar)