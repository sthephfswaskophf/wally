#williammarques
#https://github.com/swaskophf

#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip instal....)
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = [
'Marcio Cardoso de Freitas',
'Luiz Alberto Dutra',
'José Ronaldo Rodrigues Silveira',
'Luiz Marcelo Pinho Farias',
'Tiago Loureiro',
'Faiblan Ferreira Dos Santos',
'Benicio De Almeida Neto',
'Simone Pereira Schneider',
'Alessandro Marcos Da Costa',
'Fernando Alves De Oliveira',
'Karen Cristina Ferreira Da Rocha',
'Helcius Lorival Francisco',
'Gilberto Da Silva Vieira',
'Marcela De Oliveira Appel Dos Santos',
'Luiz Alberto Dame Schuch',
'Nadir Mendes Turchetto',
'Luiz Augusto Do Nascimento Leme',
'Ivanilda Bueno Godoy Goulart',
'Eduardo Nery Maiettini',
'Eva Solange Dos Santos Leite Martins',
'Clauciane Terezinha Kubereski',
'Daniele Borges De Souza Lima',
'Eva Moreira Ramos',
'Jean Kevin Da Rosa Frana',
'Alexander Marcelo Cardoso',
'Clarice Adriane Neima Dos Santos',
'Jacira De Fatima Lima Ferreira',
'Andreia Cristina Cardoso De Camargo',
'Carla Alessandra Rodrigues Da Silva',
'Alexandro Manoel Mattoso',
'Jamira Lindocir Da Silva',
'Hednilton Mendes De Morais',
'Antonio Carlos Camargo',
'Marcos Antonio Gomes',
'Feliphe Ricardo Rainerte Da Silva',
'Ana Marcia Noga',
'Marcia Matias Pires',
'Juliano Cornelius Salles',
'Fabiano Da Rosa',
'Adacir De Oliveira',
'Eduardo Caetano De Souza',
'Ana Maria Eleuterio',
'Jean Kevin Da Rosa Frana',
'Juliano Cornelius Salles',
'Jefferson Luiz Da Silva',
'Adilson Castro',
'Luiz Augusto Do Nascimento Leme',
'Joao Augusto Pereira',
'Everton Luis Stumpf',
'Marcelo Silvano Roque',
'Neida Marisa Ferreira Dos Santos',
'Edna Ramos',
'Claudio Sergio Tedeschi',
'Paulo Henrique Da Silva',
'Jose Severino Da Silva',
'Denis Da Rosa',
'Rafael Jorge Carraro De Carvalho',
'Tania Da Silva',
'Ivanilda Bueno Godoy Goulart',
'Tania Da Silva',
'Clerio Luiz Petricovski',
'Devair Pedro Pozzobom',
'Hednilton Mendes De Morais',
'Eduardo Cardoso Filho',
'Giancarlo Muraro',
'Ivanilda Bueno Godoy Goulart',
'Luiz Carlos Dalla Vecchia',
'Rubens De Mello',
'Anthony Basil Ritchie',
'Ioni Da Rosa Vitoria',
'Alinor Antonio Veiga',
'Carolina Teles Campos Do Nascimento',
'Michele Biscaglia Mozzaquatro',
'Ana Paula Tristao',
'Alexandro Manoel Mattoso',
'Jamira Lindocir Da Silva',
'Celso Do Amaral ',
'Marcia Matias Pires',
'Paulo Roberto Sibilla Rodrigues',
'Dircelia Maria Machado',
'Cantarelly Quiarelli Dos Santos',
'Emilene Boll',
'Jose Severino Da Silva',
'Ediomara Aparecida Bueno',
'Antonio Marcos Lopes Da Silva',
'Clovis Souza Coelho',
'Bruno Almeida Lopes',
'Flavio Jose Chornobay',
'Angelo David Dal Gobbo',
'Denis Da Rosa',
'Carlos Felizardo',
'Cristiano Assis Do Santos',
'Alfredo Grams',
'Alvaro Alex Rathke',
'Iago Guisolfi De Moura',
'Andre Adilson Sabala De Andrade',
'Daniel Heitor Branco Da Silva',
'Sandro Alex Ferreira Da Silva',
'Agenor Tibincoski',
'Fernando Henrique Silva',
'Fernando Henrique Silva',
'Deine Luan Alves De Lima',
'Clederson Renato C Borrasca',
'Salete Gris Seibt',
'Bruno Enrico Marcoccia',
'Dayana Renata Mendes Pereira',
'Carmen Lucia Hernandes Mendes',
'Ana Lucia Mattos De Borba',
'Fabio Eufrazio Barbosa',
'Alexandro Lochette Damaceno',
'Valdir Mallmann',
'Alice Harumi Yoshida',
'Aldonei Dias Dos Reis',
'Adilson Farias',
'Eduardo Ferronato Oliver',
'Edivania Ferreira Da Paz',
'Brisa Kurtz Fonseca',
'Ana Emilia Hardt Soares',
'Adelmo Rosa Da Silva',
'Evaldo Peters',
'Everson Procopio Da Silva',
'Daniela Roza',
'Bruna Eccel Goulart Maier',
'Fabricio Matesco',
'Fabio Renato Torres Lopes',
'Carlos Eduardo Roesel',
'Cleiton Elessandro de Oliveira',
'Anderson Prestes Silva',
'Alice Mold',
'Nilse Conink',
'Georges De Reis Vitorino',
'Silvia Marina Dos Santos Borges',
'Claudia Andrey Agostini',
'Jose Alberto Duarte Tessmer',
'Ederval Scottini',
'Anderson Prestes Silva',
'Cintia Imhof Gallassini',
'Silvia Marina Dos Santos Borges',
'Fabio Renato Torres Lopes',
'Cláudio Carvalho',
'Eder Fermino Correa',
'Gilberto Damazio',
'Everson Guerra de Moraes',
'Rosili Souza Leite',
'Edgar Benedetti',
'Elis Angela Gomes Neves',
'Adilson Alves',
'Bruna Eccel Goulart Maier',
'Charles Bombasar',
'Luis Felipe Puhlmann Da Luz',
'Ivanilda Bueno Godoy Goulart',
'Gessy Alcina Furlin Tomasi',
'Fabio Seoane Soalheiro',
'Bruce Marafon',
'Felipe Volfon',
'Nelson Ricardo Lana',
'Elaine Cristina Rodrigues Barbosa',
'Alvaro Laurentino',
'Rosili Souza Leite',
'Carlos Eduardo Roesel',
'Gisela Paludo',
'Cristiano Fortes Zanin',
'Dharlyn Furtado Passos',
'Sergio Toldo Machado',
'Daniel Diedrich',
'Daniel Diedrich',
'Alessandra Furtado Gadelha',
'Edvan De Souza Pereira',
'Claudinei Dos Santos Da Silva',
'Carlos Alberto Acosta Mafuz',
'ANTONIO FERNANDO COUGO LOUZADA',
'Ingrid Buschermoehle Juskow',
'Lucelia Maria Perotto Guedes',
'Mariluci Dalepiane',
'Elda Maria Bampi',
'Angelica Salete Da Rosa',
'Anastacio Junior Cedric Alves De Almeida',
'Breno Luiz Muller',
'Jaira Cristina Dessoy',
'Lindalva Lima De Oliveira',
'Diego Fernandez Rodrigues',
'Fabricio Philippi',
'Bruno Adriano',
'Andre Luis Grando',
'Cristiano Oliveira Goncalves',
'Anderson Seib Da Silva',
'Valdecir Freitas De Oliveira',
'Cristiano Oliveira Goncalves',
'Sonia Paula Moniz Botelho',
'Cristiane Silveira Alves Da Costa',
'Charles Dalcin',
'Jaira Cristina Dessoy',
'Brinalda Vega De Menezes',
'Luiz Carlos Dalla Vecchia',
'VALTER LUIZ SCHNEIDER BRASIL',
'Laercio De Souza',
'Denise Remiao Lopes',
'Carlos Pacheco Machado',
'Luisandro Da Rosa Da Silva',
'Edite Do Amaral',
'Andre Dias Andrade',
'Bayron Dos Santos Cateno',
'Fabiana Pereira Correa',
'Fabiano Pereira da Silva',
'Eliziane Regina Alves Aguiar',
'Ivan Ribeiro Dos Santos',
'Lisandra Casa Nova Casa Nova',
'Edison Pinto Rodrigues',
'Jefferson Luiz Da Silva',
'Paulo Roberto Silva Da Silva',
'Clea Maria Da Silva Lobo',
'Charles Bombasar',
'Ane Mari Klein',
'Francisca Vieira Da Silva',
'Wanderley Meirelles',
'Fabio Santos Ribeiro',
'Adriano Madeira De Souz',
'Valdecir Freitas De Oliveira',
'Salete Gris Seibt',
'Antonio Augusto Dias Cidade',
'Daniela Mari Pezzi',
'Gilberto Bernardo Boeira Marsiglio',
'Edson Rodrigo Santana Gonzales',
'Claudio Diefenthaler',
'Elirio Fernando Caetano',
'Everton Luis Stumpf',
'Rosilda Da Siqueira',
'Antonio Ernesto Wiering Carmel',
'Aquiles Armichi',
'Paulo Adriano Krutzmann',
'Vitor Eckert Cassol',
'Elisangela Moraes Raymundo',
'Fabio Astrada de Dorneles',
'Agnaldo Ferreira Dos Santos',
'Crisciano Da Silva Martins',
'Cristiane Fogaca Rodrigues',
'Gilson Arigony Irigaray',
'Everton Da Silva Stelter',
'Cleber Martins',
'Crisciano Da Silva Martins',
'Valdoir Jacobsen Goncalves',
'Armindo Celestino Galvão',
'Nelson Casagrande',
'Edina Da Silva',
'Giordana Silva De Mello',
'Priscila Pires De Andrade Lima',
'José Ronaldo Rodrigues Silveira',
'Fernando Rodrigues Silva',
'Adao Ervidio Dos Santos',
'Roberval De Alan Barros',
'Adriano Alves Dos Santos',
'Dirceu Peres Da Silva',
'Charles De Oliveira Batista',
'Ana Regina Selin Moreira',
'Andrea De Gasperi Rosa',
'Gicele Machado Dos Reis Tomasini',
'Roberto Leandro Boeira',
'Decio Antonio Corbellini',
'Fabio Gustavo Eidelwein',
'Andre Marques Silva',
'Juliana Wabner Dos Santos',
'Valdir Mallmann',
'Gustavo Carvalho Dos Santos',
'Ari Fernandes Da Luz',
'Angelica Martins Muller',
'Elirio Fernando Caetano',
'Alexandre Mota Machado',
'Cristiano Cichocki',
'Sandro Alex Ferreira Da Silva',
'Dirceu Peres Da Silva',
'Edson Rodrigo Santana Gonzales',
'Carla Catarina Ritter',
'Dilson Edir Marx',
'Faustino Luiz Panciera',
'Valdecir Freitas De Oliveira',
'Andre Trein Rodrigues',
'Antonio Marcos Lopes Da Silva',
'Anderson Gomes Caldeira',
'Marcos Vinicius Zonta Salermo',
'Ciro Becker Justo',
'Jose Americo Da Rosa',
'Alan Carlos Rocha Pires',
'Ana Maria Orselli Zannin',
'Andre Luiz Martins Epifanio',
'Everton Goncalves Brum',
'Fernando Matos Da Silva',
'Renato Santanna Fernandes',
'Elena Ilse Reuse',
'Airton Lemos Marques',
'Bruna Bedin De Oliveira',
'Francisco Ataides Guedes',
'VALTER LUIZ SCHNEIDER BRASIL',
'Claudiomir Francisco Rech Da Silva',
'Ilka Da Conceicao Goncalves',
'Luciano Da Silva Leite',
'Fabio Santos Ribeiro',
'Rogerio Pageno',
'Gabriel Angel Valiente Santana',
'Cleber Martins',
'Nelson Casagrande',
'Eduardo Pereira Da Cunha Silva',
'Gilberto Damazio',
'Paolo Banti',
'Roger Viana Da Silva',
'Danilo Bastos Menna',
'Eva Wojcickoski Brasil',
'Priscila Pires De Andrade Lima',
'Alcione Correa Da Costa Prates',
'Roberto Leandro Boeira',
'Anderson Sassi De Souza',
'Fabio Renato Carvalho',
'Rogerio De Freitas Ribeiro',
'Ciro Becker Justo',
'Paulo Roberto da Silva Oliveira',
'Ernani Duarte Junior',
'Amanda Carolina Verch',
'Gustavo Carvalho Dos Santos',
'Bernardo De Moraes',
'Giuliano Makowski Giacomazzi',
'Crisciano Da Silva Martins',
'Rosilda Da Siqueira',
'CHARLES SCHERER DO COUTO',
'Antonio Roberto Vianna Santos',
'Darci Da Silva',
'Terezinha Dos Santos Correa',
'Daniela Alexandra Razini',
'Carmen Lucia Silva Vargas',
'JOHN OLAF JOHNSEN COLLARES',
'Gilmar Jose Da Silva',
'Daniel Luz Dos Santos',
'Mauricio De Oliveira Longaray',
'Bernardo De Moraes',
'Rubem Possolino',
'Alex Sandro Paz Da Rosa',
'Daniela Medeiros Da Silva',
'Claudio Speth',
'Diego Dos Santos Bernardo',
'Elenice Pires Franco',
'Geovana Vagner Machado',
'Geovana Vagner Machado',
'Diogo Morador Brasil',
'Armando De Alencar Aperta',
'Eder Soehn Zanini',
'Ederson Rodrigues Abreu',
'Eleonor Angelica Cardoso De Souza',
'Fernando Antonio Cossio Martins',
'Iara Pasa',
'Priscila Pires De Andrade Lima',
'Leonardo Augusto Klein',
'Cilon Fernandes Da Rosa',
'Silveria Ruppenthal Da Conceicao',
'Denise Flebbe',
'Fernando Martins Muniz',
'Luciano Castro Foques',
'Andressa Caroline Horn',
'João Inocêncio Rodrigues',
'Jacira De Fatima Lima Ferreira',
'Claudio Russowsky',
'Elvidio Da Silva Moreira',
'Marcio Fernandez Vieira',
'Marcio Fernandez Vieira',
'Claudio Antonio Souza De Avila',
'Diogo Schuller Siqueira',
'Marcio Fernandez Vieira',
'Joana Maria Da Silva',
'Aline Oliveira Ferreira',
'Guilherme Spat Peres',
'Guilherme Spat Peres',
'Valter Antonio Dalcin',
'Osmar Carvalho Lemos',
'Emerson Matos Bandeira',
'Luiz Alberto Dame Schuch',
'Denise Flebbe',
'Cristiano Da Silva',
'Bento Goncalves Marques Rocha',
'Alessandro Dos Santos Almeida',
'Gilmar Alex Gazoni',
'Gilney Telles De Freitas',
'Carina Juliana Correa Estraich',
'Jose Maria Pereira Filho',
'Evanilda Bastos Osmainschi',
'Abel Vanderlei Quevedo Da Silva',
'Anderson Lisboa Rodrigues',
'Lucas Michel Costa',
'Marçal Werhli',
'Daniel Victor Rodrigues',
'Fernanda Kajenski Alves',
'Cicero Yuri Jader Pereira',
'Joao Manoel Castro De Almeida',
'Joao Manoel Castro De Almeida',
'Eliziane Regina Alves Aguiar',
'Daiane Dos Santos Moreira',
'Marcelo Sumariva',
'Eder Soehn Zanini',
'Joao Cabreira Bitencurt',
'SELMO FRANCISCO BAHDE GONZAGA',
'Carlos Alberto Acosta Mafuz',
'Pedro Ademir Zamboni',
'Everton Rodrigues Silveira',
'Renata Goncalves Krieger',
'Andre Muller De Araujo',
'Pedro Ademir Zamboni',
'Cladimir Amilton Wojcik',
'Antonio Roberto Vianna Santos',
'Ioni Da Rosa Vitoria',
'Iara Pasa',
'Geimison Fernandes Costa',
'Dyulli Camila Da Silva Tome',
'Renata Goncalves Krieger',
'Elisangela Regina Barazetti',
'André Ferreira da Silva',
'Paulo Cesar De Paiva',
'Loir Jose Cigolini',
'Felipe Saldanha',
'Darlan Butkiewicz',
'Silvia Marina Dos Santos Borges',
'Rosildo Francisco Da Silva',
'Daniela Roza',
'Vitor Treptow',
'Valdoir Jacobsen Goncalves',
'Fabiana Pereira Correa',
'Jose Cleo Siqueira Oliveira',
'Darlan Butkiewicz',
'Claudio Speth',
'Edison Pinto Rodrigues',
'Ivan Ribeiro Dos Santos',
'Rafael Mattos',
'Fabio Galvao Fioravante',
'Cristiano Dos Santos Sbroglio',
'Giordana Silva De Mello',
'Clauduio Rogerio Dos Santos',
'Delton Antonio Krinski',
'Mario Sergio Taques',
'Patricia Vargas Henriques',
'Danilo Bastos Menna',
'Caciane Patricia Da Silva',
'Bayron Dos Santos Cateno',
'Branca Melinda Luchsinger Pereira',
'Alexsandro Monteiro Da Silva',
'Bernadete Socorro Diniz',
'Enock Rodrigues Da Silva Jr',
'Ahizechukwu Chinonso Samuel Emele'
]

#Mensagem - Mensagem que sera enviada
mensagem = 'Tem boa notícia chegando no seu WhatsApp, '
mensagem2 = '! Estamos iniciando a semana da regularização de dívidas! E aí, que tal ver o que podemos fazer por você? Confira as condições especiais de pagamento! Responda essa mensagem e vamos conversar! Rama Advogados Associados, representante do Canal Judicial do Banco Santander. Atendimento facilitado via WhatsApp ou se preferir ligue para *4007.2279* das 9h - 18h de segunda à sexta-feira.'


#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagem,mensagem2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(str(mensagem) + str(contato) + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)


#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem,mensagem2) 
    time.sleep(1)