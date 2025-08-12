""" A codificação ZENIT POLAR é um tipo de cifra de substituição simples na qual as letras de duas palavras ou grupos de letras são usadas para substituir uma pela outra. No caso específico de "ZENIT POLAR", cada letra em "ZENIT" é substituída pela letra correspondente em "POLAR" e vice-versa. Esse tipo de cifra é bidirecional e simétrica, significando que a mesma substituição é usada para codificar e decodificar mensagens.

Observe como a substituição funciona para cada letra.

**Z** é substituída por **P** e **P** por **Z**.
**E** é substituída por **O** e **O** por **E**.
**N** é substituída por **L** e **L** por **N**.
**I** é substituída por **A** e **A** por **I**.
**T** é substituída por **R** e **R** por **T**.

Todas as outras letras que não estão incluídas na cifra são deixadas inalteradas. A cifra ZENIT POLAR é relativamente simples e não oferece uma segurança robusta para padrões modernos, mas é um exemplo interessante de manipulação básica de texto e pode ser usada para ilustrar conceitos de criptografia em contextos educacionais ou para diversão.
"""

def zenit_polar_replace(text):
    # Aplicar a codificação zenit-polar utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'), # Minúsculas
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')] # Maiúsculas
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
    # Entrada da frase e aplicação da codificação zenit-polar
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase_title = phrase.title() # Primeira letra de cada palavra em maiúscula

    # Dividir a frase em palavras
    words = phrase_title.split()

    # Processar cada palavra na lista usando ZENIT-POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    # Juntar as palavras codificadas de volta em uma frase
    coded_phrase = ' '.join(coded_words)
    print("Original Phrase:", phrase)
    print("Title ", phrase_title)
    print("Coded:", coded_phrase)

if __name__ == "__main__":
    main()