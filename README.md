# Bot Patin Maguin

Esse projeto de bot para Discord tem a intenção apenas de praticar lógica e organização de projetos com Python. Não tenho pretensão, por enquanto, de deixar o bot disponível para outros servidores além do meu servidor pessoal, que utilizo com meus amigos.

Dito isso, esse bot foi inspirado em um personagem original que surgiu como uma piada interna do meu grupo: um pato mago que não parecia nada com um pato. Quando tive a ideia de criar um bot para moderação e algumas funções de diversão para o servidor, esse personagem foi o primeiro que me veio à cabeça.

O bot poderá ser utilizado para moderação, organização do servidor, jogos e também eventos online que acontecem no servidor.

Como o bot foi criado apenas para um servidor, ele tem funcionalidades que fazem sentido para os usuários desse servidor. As próximas features provavelmente virão de sugestões desses mesmos usuários ou de qualquer pessoa que gostar do projeto. Aceito todo tipo de contribuição também.

Por enquanto, o bot conta com as seguintes funcionalidades.

## Comandos com `.`

- `.limpar` + número → apaga n mensagens do canal de texto atual.
- `.oi` → o bot responde com um "Olá!" bem animado.
- `.falar` + mensagem → o bot fala a mensagem que o usuário quiser.
- `.dado` + número → gira um dado com n faces e mostra o resultado.

## Comandos com `/`

- `/avatar` + usuário → mostra a foto de perfil do usuário escolhido.
- `/frase` + mensagem + usuário → envia a mensagem digitada no canal de texto com o nome `#frasesinhas`, formatada como uma citação, e marca o usuário escolhido.

### Comandos relativos ao bingo

Geralmente, antes de assistir a um filme, geramos uma cartela de bingo em algum site para fazer previsões sobre coisas que podem acontecer durante o filme. Se alguém fechar uma fileira completa, todos ganham.

Então resolvi fazer isso no próprio bot do Discord, para que todos possam dar seus palpites ao mesmo tempo, sem precisar esperar o host para adicionar e validar os palpites.

- `/criarbingo` + título → inicia uma sessão de bingo 5x5 com 24 espaços (o espaço do meio é `FREE`).
- `/criarbing` + título → inicia uma sessão de bingo 4x4 com 16 espaços (sem `FREE`).
- `/palpite` + mensagem → adiciona o palpite à cartela.
- `/mostrarpalpites` → mostra a lista de palpites com um número de identificação (ID).
- `/removerpalpite` + ID do palpite → remove o palpite com base no ID, caso seja do mesmo usuário que executou o comando. **Em breve.**
- `/gerarcartela` → embaralha os palpites e gera a imagem da cartela. **Em breve.**
