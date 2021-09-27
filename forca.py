import os

class Forca:
    
    def saida(self, vInicial=0, vFinal=3):
        '''
        Cria a animação de saída do programa
        '''
        i = 0
        while vFinal > vInicial:
            if i == 0:
                msg = '≤≤≤≤≤≤'
            elif i == 1:
                msg = '≡≡≡≡≡≡'
            else:
                msg = '≥≥≥≥≥≥'
                i = -1
            i += 1
            os.system('cls')
            print('Finalizando ', msg)
            vInicial += 1
        os.system('cls')
        input('Obrigado por usar nosso aplicativo!\nTNT Solutions ©® 2021.\n')

    def limpa_tela(self):
        '''
        Método para limpar a tela do terminal
        '''
        os.system('cls')

    def menu(self, textos, cabecalho=''):
        '''
        Método para imprimir um menu na tela
        '''
        # chama o método interno para limpar a tela
        self.limpa_tela()
        # Ponta superior esquerda do menu
        pse = '╔'
        # Ponta superior direita do menu
        psd = '╗'
        # Ponta inferior esquerda do menu
        pie = '╚'
        # Ponta superior direita do menu
        pid = '╝'
        # Reta do menu
        ret = '═'
        # Lateral do menu
        lat = '║'
        # procura a maior string no array
        maior = 0
        # percorre todo o array do parâmetro
        for item in textos:
            if len(item) > maior:
                # pega a string com a maior quantidade
                maior = len(item)
        # multiplica o caracter de reta pelo tamanho da maior string + 2 
        ret *= maior + 2
        # imprime a parte de cima do menu
        print(f'{pse}{ret}{psd}')
        # se tiver cabeçalho no menu
        if cabecalho != '':
            # cabeçalho esquerdo
            cae = '╠'
            # cabeçalho direito
            cad = '╣'
            # divide o valor por dois, e trunca para dividir o cabeçalho no menu
            espacos = ' ' * int((maior - len(cabecalho))/2)
            # ajusta o cabeçalho no topo do menu
            # if len(cabecalho) > 1:
            #     print(f'{lat} {espacos}{cabecalho}{espacos}  {lat}')
            # else:
            #     # Se for somente um caracter, precisa descontar um caracter para ajustar corretamente
            print(f'{lat} {espacos}{cabecalho}{espacos} {lat}')
            # imprime a parte final do cabeçalho
            print(f'{cae}{ret}{cad}')
        for texto in textos:
            # retira o <enter> que possa existir na string, que desconfigurará o menu
            texto = texto.replace('\n', '')
            # recupera o tamanho da string
            espacos = ' ' * (maior - len(texto))
            # para todas as strings de parâmetro imprime no menu
            print(f'{lat} {texto}{espacos} {lat}')
        # imprime a parte de baixo do menu
        print(f'{pie}{ret}{pid}') 

    def grafico_jogo_velha(self, _estagio, _palavra_secreta, _letras_acertadas,_letras_chutadas,_rodada):

        self.menu(['Jogo da Forca',f'Dica: a palavra secreta tem {len(_palavra_secreta)} letras',f'{_rodada + 1}ª Rodada'])
        p = [' ',' ',' ',' ',' ',' ']
        if _estagio == 0:
            p[0] = '^'
        elif _estagio == 1:
            p[0] = 'o'
        elif _estagio == 2:
            p[0] = 'o'
            p[1] = '/'
        elif _estagio == 3:
            p[0] = 'o'
            p[1] = '/'
            p[2] = '|'
        elif _estagio == 4:
            p[0] = 'o'
            p[1] = '/'
            p[2] = '|'
            p[3] = '\\'
        elif _estagio == 5:
            p[0] = 'o'
            p[1] = '/'
            p[2] = '|'
            p[3] = '\\'
            p[4] = '/'
        else:
            p[0] = 'o'
            p[1] = '/'
            p[2] = '|'
            p[3] = '\\'
            p[4] = '/'
            p[5] = '\\'
        print('Letras digitadas: ', _letras_chutadas)
        print('\nPalavra secreta: ', _letras_acertadas)
        print(f'╔══╗')
        print(f'║  {p[0]}')
        print(f'║ {p[1]}{p[2]}{p[3]}')
        print(f'║ {p[4]} {p[5]}')
        print(f'╚════')

    def escolher_palavra(self, _numero):
        '''
        Método escolhe uma palavra baseado no número da linha do arquivo words.txt. 0 até 2287
        '''
        with open('words.txt') as file_object:
        # lê todas as linhas
            _lista = file_object.readlines()
            # retorna uma linha baseada no número passado como parâmetro
        return _lista[_numero].strip()

    def numeroAleatorio(self, _min, _max, tipo=0):
        '''
        Método retorna um número aleatório entre os parâmetros [_min] e [_max], tipo é para o retorno ser
        float ou int. O padrão é um número inteiro!
        '''
        import random
        # retorna um número aleatório do tipo int 
        if tipo == 0:
            return random.randint(_min, _max)
        # retorna um número aleatório do tipo float
        elif tipo == 1:
            return random.random() + random.randint(_min, _max)
        else:
            return tipo

    def jogo_velha(self):
        '''
        Jogo da velha - Lista de palavras do seguinte endereço, somente aquelas com cinco letras ou mais
        https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/
        '''
        palavra_secreta = self.escolher_palavra(self.numeroAleatorio(0, 2287))
        
        letras_acertadas = []
        for i in range(len(palavra_secreta)):
            letras_acertadas.append("_")
        # lista com as palavras que foram digitadas
        letras_chutadas = []
        # numero de chances
        chance = 0
        parabens = False
        while(chance < 6):
            self.grafico_jogo_velha(chance, palavra_secreta, letras_acertadas, letras_chutadas, len(letras_chutadas))
            f = True
            while f == True:
                chute = input("Digite a letra: ").upper()
                if chute in letras_chutadas:
                    print('Letra já digitada!')
                else:
                    f = False
            # pega só a primeira letra digitada e exclui o espaço
            chute = chute.strip()[0:1]
            index = 0
            f2 = False
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra.upper()
                    f2 = True
                index += 1

            if f2 == False:
                chance += 1

            letras_chutadas.append(chute.upper())
            if '_' not in letras_acertadas:
                parabens = True
                break
        
        if parabens == True:
            self.grafico_jogo_velha(chance, palavra_secreta, letras_acertadas, letras_chutadas, (len(letras_chutadas)-1))
            print(f'Parabéns você acertou a palavra!\nFim da partida...')
        else:
            self.grafico_jogo_velha(chance, palavra_secreta, letras_acertadas, letras_chutadas, (len(letras_chutadas)-1))
            print(f'A palavra secreta era: {palavra_secreta.upper()}\nFim da partida...')

while True:
    jogo = Forca()
    jogo.jogo_velha()
    if input('Jogar novamente? <enter> para continuar.\n') == '':
        jogo.jogo_velha()
    else:
        jogo.saida(0,9)
        break
        