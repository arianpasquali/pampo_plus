# -*- coding: utf-8 -*-
class PortuguesePatterns(object):

    common_family_names = [
        u"Silva",
        u"Santos",
        u"Ferreira",
        u"Pereira",
        u"Oliveira",
        u"Costa",
        u"Rodrigues",
        u"Martins",
        u"Jesus",
        u"Sousa",
        u"Fernandes",
        u"Gonçalves",
        u"Gomes",
        u"Lopes",
        u"Marques",
        u"Alves",
        u"Almeida",
        u"Ribeiro",
        u"Pinto",
        u"Carvalho",
        u"Teixeira",
        u"Moreira",
        u"Correia",
        u"Mendes",
        u"Nunes",
        u"Soares",
        u"Vieira",
        u"Monteiro",
        u"Cardoso",
        u"Rocha",
        u"Neves",
        u"Coelho",
        u"Cruz",
        u"Cunha",
        u"Pires",
        u"Ramos",
        u"Reis",
        u"Simões",
        u"Antunes",
        u"Matos",
        u"Fonseca",
        u"Machado",
        u"Araújo",
        u"Barbosa",
        u"Tavares",
        u"Lourenço",
        u"Castro",
        u"Figueiredo",
        u"Azevedo",
        u"Melo"
    ]

    titles = [
        u"grão-mestre",
        u"papa",
        u"duque",
        u"duquesa",
        u"conde",
        u"condessa",
        u"presidente",
        u"rei",
        u"raínha",
        u"príncipe",
        u"princesa",
        u"marquês",
        u"marquesa",
        u"secretário",
        u"secretária",
        u"bispo",
        u"visconde",
        u"viscondessa",
        u"ministro",
        u"ministra",
        u"barão",
        u"baronesa",
        u"general",
        u"tenente",
        u"deputado",
        u"deputada",
        u"governador",
        u"governadora",
        u"capitão",
        u"capitã",
        u"diretor",
        u"diretora",
        u"primeiro",
        u"primeira",
        u"sargento",
        u"ex",
        u"filho",
        u"filha",
        u"irmão",
        u"irmã",
        u"pai",
        u"mãe",
        u"tio",
        u"tia",
        u"padrinho",
        u"madrinha",
        u"sobrinho",
        u"sobrinha",
        u"afilhado",
        u"afilhada",
        u"avó",
        u"avô",
        u"neto",
        u"neta",
        u"enteado",
        u"enteada",
        u"padrasto",
        u"madrasta",
        u"vice"
    ]

    preprositions = [
        u"da",
        u"das",
        u"dos",
        u"do",
        u"de",
        u"para",

    ]

    tags_exclusions =[
        u"AUX",
        u"DET",
        u"ADJ",
        u"PRON",
        u"ADV",
        u"ADP",
        u"VERB",
        u"SYM",
        u"CCONJ",
    ]

    starters = [
        u"A",
        u"As",
        u"O",
        u"Os",
        u"Em",
        u"Aos",
        u"Ao",
        u"No",
        u"Na",
        u"Nos",
        u"Nas"
]

    stopwords = [
    u"Janeiro",
    u"Fevereiro",
    u"Março",
    u"Abril",
    u"Maio",
    u"Junho",
    u"Julho",
    u"Agosto",
    u"Setembro",
    u"Outubro",
    u"Novembro",
    u"Dezembro",
    u"Diário",
    u"Semanal",
    u"Mensal",
    u"Minutos",
    u"Meses",
    u"Ano",
    u"Anos",
    u"Hoje",
    u"Anexo",
    u"Abertura",
    u"Atestado",
    u"Ata",
    u"Adoção",
    u"Atualização",
    u"Às",
    u"À",
    u"Capa",
    u"Convite",
    u"Compromisso",
    u"Condecoração",
    u"Convocatória",
    u"Cartão",
    u"Causa",
    u"Comunicação",
    u"Corrupção",
    u"Convergência",
    u"Decreto",
    u"Ditadura",
    u"Democacia",
    u"Democrata",
    u"Estrutura",
    u"Ficha",
    u"Fax",
    u"Fixação",
    u"Futuro",
    u"Gabinete",
    u"Glória",
    u"Harmonia",
    u"Iniciado",
    u"Instalação",
    u"Ibidem",
    u"Inventariação",
    u"Irregularidades",
    u"Internet",
    u"Lda",
    u"Manutenção",
    u"Nomeado",
    u"Obediência",
    u"Petição",
    u"Passaporte",
    u"Proposta",
    u"Programa",
    u"Proibição",
    u"Paz",
    u"Publicação",
    u"Questionário",
    u"Quadro",
    u"Relatório",
    u"Redução",
    u"Reorganização",
    u"Revolução",
    u"República",
    u"Reequilíbrio",
    u"Reação",
    u"Sessão",
    u"Testamento",
    u"Tolerância",
    u"Término",
    u"Vitória",
    u"Visita",
    u"Aceite",
    u"Comprometo",
    u"Cabe",
    u"Coloca",
    u"Conhecemos",
    u"Casado",
    u"Considerava",
    u"Desejo",
    u"Devíamos",
    u"Escolhiam",
    u"Executa",
    u"Faça",
    u"Fica",
    u"Interrompidas",
    u"Indicar",
    u"Incluído",
    u"Leva",
    u"Morrer",
    u"Ouvistes",
    u"Prestaste",
    u"Praticou",
    u"Pressiona",
    u"Pensa",
    u"Poder",
    u"Podes",
    u"Revolta",
    u"Sabe",
    u"Ser",
    u"Ter",
    u"Toque",
    u"Toma",
    u"Trata",
    u"Vens",
    u"Verificou",
    u"Viver",
    u"Vivemos",
    u"Venho",
    u"Aproveitamento",
    u"Cuidado",
    u"Decerto",
    u"Desta",
    u"Desenvolvimento",
    u"Lançamento",
    u"Levantamento",
    u"Muitos",
    u"Muitas",
    u"Nessa",
    u"Nesse",
    u"Nessas",
    u"Nesses",
    u"Nestes",
    u"Neste",
    u"Nesta",
    u"Nestas",
    u"Noutro",
    u"Outros",
    u"Outro",
    u"Outra",
    u"Outras",
    u"Onde",
    u"Poucos",
    u"Poucas",
    u"Perante",
    u"Pela",
    u"Recém",
    u"Tal",
    u"Vários",
    u"Várias",
    u"Vós",
]
