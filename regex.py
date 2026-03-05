import re
'''
METACARACTERES
    REPRESENTANTES
        . PONTO (O NECESSITADO)
        [ ] LISTA
        [^] LISTA NEGADA
    QUANTIFICADORES
        ? OPCIONAL
        * ASTERISCO
        + MAIS
        {n,m} CHAVES
    ANCORAS
        ^ CIRCUNFLEXO
        $ CIFRÃO
        \b BORDA
    OUTROS
        | OU
        ( ) GRUPO
        \ ESCAPE
        \1 RETROVISOR
'''
representante = re.compile(r'.eclado')
procura = representante.search('teclado, Teclado, eclado, Mesclado')
resultado = procura.group()
print(resultado)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
areaCode = mo.group(1)
mainNumber = mo.group(2)

print(areaCode)
print(mainNumber)

#Fazendo a correspondência de vários grupos com pipe
#Localiza a primeira ocorrência
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('fergunson Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
moBat = batRegex.search('Batmobile lost a wheel')
print(moBat.group())

#? Significa que (wo) é opcional
batRegex2 = re.compile(r'Bat(wo)?man')
moBat2 = batRegex2.search('The adventures of Batman')
print(moBat2.group())
moBat3 = batRegex2.search('The adventures of Batwoman')
print(moBat3.group())

# * Significa que deve localicar quantas (wo) tiver
batRegex3 = re.compile(r'Bat(wo)*man')
mo1 = batRegex3.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex3.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex3.search('The Adventures of Batwowowowoman')
print(mo3.group())

# + significa que pelo menos 1 (wo) é exigido \d+ = Um ou mais dígitos
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# {3} significa 3x o (Ha)
haRegex = re.compile(r'(Ha){3}')
#{1,3} significa 1,2 ou 3 (Ha)
haRegex2 = re.compile(r'(Ha){1,3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)
mo3 = haRegex2.search('HaHa Ha')
print(mo3.group())

#Por padrão é greedy (Goloso) utilize o ? no final para pegar o mínimo
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

#FindAll
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex2.findall('Cell: 415-555-9999 Work: 212-555-0000'))

'''
\d Qualquer dígito de 0 a 9. 
\D Qualquer caractere que não seja um dígito de 0 a 9. 
\w Qualquer letra, dígito ou o caractere underscore. (Pense nisso como uma correspondência de caracteres de “palavra”.) 
\W Qualquer caractere que não seja uma letra, um dígito ou o caractere underscore.
\s Qualquer espaço, tabulação ou caractere de quebra de linha. (Pense nisso como uma correspondência de caracteres de “espaço”.)
\S Qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha.
'''

#^ significa que ser quer o contrário
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#^ também é utilizado para informar que inicia com uma palavra 
beginsWithHello = re.compile(r'^Hello')
# ! no final indica que a frase termina com a palavra
#A string r'^\d+$' de expressão regular corresponde a strings que comecem e terminem com um ou mais caracteres numéricos.
finishWithWorld = re.compile(r'world!$')
print(beginsWithHello.search('Hello world!'))
print(finishWithWorld.search('Hello world!'))

# O .(ponto) é um caracatere coringa
#Podemos usar ponto-asterisco (.*) para indicar “qualquer caractere”.
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Fabio Last Name: Reis')
print(mo.group(1), mo.group(2))

'''
RESUMO:
• ? corresponde a zero ou uma ocorrência do grupo anterior. 
• * corresponde a zero ou mais ocorrências do grupo anterior. 
• + corresponde a uma ou mais ocorrências do grupo anterior. 
• {n} corresponde a exatamente n ocorrências do grupo anterior. 
• {n,} corresponde a n ou mais ocorrências do grupo anterior. 
• {,m} corresponde a zero até m ocorrências do grupo anterior. 
• {n,m} corresponde a no mínimo n e no máximo m ocorrências do grupo anterior. 
• {n,m}? ou *? ou +? faz uma correspondência nongreedy do grupo anterior. 
• ^spam quer dizer que a string deve começar com spam.
• spam$ quer dizer que a string dever terminar com spam. 
• . corresponde a qualquer caractere, exceto os caracteres de quebra de linha. 
• \d, \w e \s correspondem a um dígito, um caractere de palavra ou um caractere de espaço, respectivamente. 
• \D, \W e \S correspondem a qualquer caractere, exceto um dígito, um caractere de palavra ou um caractere de espaço, respectivamente. 
• [abc] corresponde a qualquer caractere que estiver entre os colchetes (por exemplo, a, b ou c). 
• [^abc] corresponde a qualquer caractere que não esteja entre os colchetes.
'''
# Use o re.I para ignorar maiúscula e minúscula
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())

#Substituindo strings com o método sub()
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#Administrando REGEX extensa
phoneRegex = re.compile(r'''
                            ( (\d{3}|\(\d{3}\))?          # código de área 
                            (\s|-|\.)?                    # separador
                            \d{3}                         # primeiros 3 dígitos 
                            (\s|-|\.)                     # separador 
                            \d{4}                         # últimos 4 dígitos 
                            (\s*(ext|x|ext.)\s*\d{2,5})?  # extensão
                            )''', re.VERBOSE)

