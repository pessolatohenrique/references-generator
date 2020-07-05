# Reference Formatter

### Sobre
A partir de uma lista de sites com artigos, o projeto gera as referências bibliográficas com as regras da ABNT. Foi utilizada a técnica de webscraping em Python 3.

### Tecnologias
- Python 3
- Webscraping
- Utilização de bibliotecas como *request* e *Beautiful Soup*

### Instalação do projeto

- Realizar o clone do projeto

        git clone https://github.com/USER/references-generator.git
        
- Instalar as dependências

        pip install -r requirements.txt
        
- Alimentar o arquivo "links.txt" com os sites utilizados nas referências bibliográficas. Cada link, deverá ser colocado em uma nova linha

        https://www.napratica.org.br/comunicacao-nao-violenta/
        https://administradores.com.br/artigos/a-importancia-da-gestao-de-pessoas-para-as-colaboradores
        https://www.rhportal.com.br/artigos-rh/os-processos-de-rh-uma-viso-estratgica/
        https://blogrh.com.br/avaliacao-de-competencias-cha/
        https://www.metadados.com.br/blog/treinamento-e-desenvolvimento/
        https://www.megacurioso.com.br/comportamento/100690-estas-sao-as-13-atitudes-que-mais-afastam-as-pessoas-do-sucesso.htm
        https://administradores.com.br/artigos/o-conhecimento-como-vantagem-competitiva-para-as-organizacoes
        https://revistapegn.globo.com/Dia-a-dia/noticia/2015/01/7-atitudes-que-afastam-o-sucesso.html
        https://www.napratica.org.br/mentalidade-de-crescimento-entenda-o-conceito/
        https://emgotas.com/2016/11/06/como-criar-a-administracao-2-0/
    
 - Executar em uma console compatível com o Python 3
 
 - Abrir em um navegador o arquivo "references.html"
 
![Referências](https://raw.githubusercontent.com/pessolatohenrique/references-generator/master/print.png "Referências")