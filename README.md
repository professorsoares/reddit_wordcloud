# Wordcloud
Este script em *Python* busca comentários postados sobre um determinado tópico (*subreddit*) no *[Reddit](https://www.reddit.com/)*.

## Uso:

1. Clone o repositório:
    
    ```python
    ! git clone https://github.com/ICA-cursos/reddit_wordcloud
    ```

2. Importe o módulo e execute o método que busca os *posts* e gera a nuvem de palavras:

    ```python
    from reddit_wordcloud import RedditWordcloud 
    RedditWordcloud.Reddit(subreddit='python', limit=100).wordcloud()
    ```

Obs: o parâmetro `subreddit` é o tópico de interesse para busca e o parâmetro `limit` é o número de *posts* que o código buscará dentro do tópico escolhido.

## *Reddit*
*Reddit* é um agregador de conteúdo determinado pela comunidade. É uma plataforma social onde os usuários enviam postagens que outros usuários 'votam positivamente' ou 'votam negativamente' com base em seu gosto. Se uma postagem receber muitos votos positivos, ela sobe no *ranking* do *Reddit* para que mais pessoas possam vê-la.

*Subreddit* é um grupo específico de postagens, como por exemplo: *[r/Python](https://www.reddit.com/r/Python/)* é um *subreddit* onde se discute somente sobre a linguagem de programação *Python*.
