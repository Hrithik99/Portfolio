from flask import Flask,request,redirect,url_for,render_template,session
import torch
from transformers import GPTNeoForCausalLM
from transformers import AutoTokenizer

app = Flask(__name__)
model_dir = 'AICamp/nlp'
tokenizer=AutoTokenizer.from_pretrained(model_dir)
print('tokenizer loaded')
# Load the model from the saved directory
model = GPTNeoForCausalLM.from_pretrained(model_dir)
print('loaded')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['input_text']
        generated = tokenizer(user_input, return_tensors="pt").input_ids
        print('tokenizrd')
        attention_mask = torch.ones(generated.shape, dtype=torch.long, device=generated.device)
        pad_token_id = tokenizer.pad_token_id
        sample_outputs = model.generate(generated, attention_mask=attention_mask, 
                            pad_token_id=pad_token_id,do_sample=True, top_k=50,
                                # bos_token='<|startoftext|>',
                                # eos_token='<|endoftext|>', pad_token='<|pad|>',
                                max_length=100, top_p=0.95, temperature=1.9, num_return_sequences=5)
        output_string = ""

        for i, sample_output in enumerate(sample_outputs):
            output_text = tokenizer.decode(sample_output, skip_special_tokens=True)
            output_string += "{}: {}\n".format(i, output_text)
        return render_template('index.html', generated_text=output_string)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)