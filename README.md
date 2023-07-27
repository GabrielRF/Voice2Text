<img align="right" alt="Voice2Text Logo" width="30%" height="auto" src="https://github.com/GabrielRF/Voice2Text/blob/master/voice2text.jpg?raw=true">

# Voice2Text

Automação em conta do Telegram para transcrever áudios em conversas privadas. [Leia mais no post](https://blog.gabrf.com/posts/WhisperPyrogram/).

## Voice2Text.py

### Credenciais

`api_id`: Obter em https://my.telegram.org/apps;

`api_hash`: Obter em https://my.telegram.org/apps.

### Modelo

Escolha o modelo usado na transcrição. O valor padrão é `base`. [Escolha o modelo no repositório oficial](https://github.com/openai/whisper#available-models-and-languages).

```python
model = whisper.load_model("base")
```

### Funções

`remove_file`: Remove o arquivo de áudio para diminuir o uso de armazenamento;

`voice_to_text`: Faz a transcrição do arquivo recebido em até 5 tentativas. Idioma selecionado: `Português`;

`download_voice`: Salva o arquivo de áudio;

`edit_message`: Edita a mensagem de texto. Usada ao finalizar a transcrição;

`send_message`: Envia uma mensagem de texto indicando o início da transcrição;

`delete_message`: Remove a mensagem de texto. Usada em caso de falha na transcrição;

`receive_voice`: Recebe a mensagem com base nos filtros definidos e executa a transcrição.
