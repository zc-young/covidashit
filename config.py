import datetime as dt
import os

from flask_babel import gettext

NATIONAL_DATA_FILE = "dpc-covid19-ita-andamento-nazionale.json"
REGIONAL_DATA_FILE = "dpc-covid19-ita-regioni.json"
PROVINCIAL_DATE_FILE = "dpc-covid19-ita-province.json"
BASE_URL_DATA = (
    "https://raw.githubusercontent.com"
    "/pcm-dpc/COVID-19/master/dati-json/"
)
URL_NATIONAL_DATA = os.path.join(BASE_URL_DATA, NATIONAL_DATA_FILE)
URL_REGIONAL_DATA = os.path.join(BASE_URL_DATA, REGIONAL_DATA_FILE)
URL_PROVINCIAL_DATA = os.path.join(BASE_URL_DATA, PROVINCIAL_DATE_FILE)
ITEN_MAP = {
    "ricoverati_con_sintomi": {
        "title": gettext("Hospitalized With Symptoms"),
        "desc": gettext(
            "# of people currently hospitalized with symptoms"
        ),
        "longdesc": gettext(
            "Total count of people currently in hospital "
            "due to coronavirus with symptoms"
        ),
        "fa": "fas fa-hospital-user"
    },
    "terapia_intensiva": {
        "title": gettext("Intensive Care Unit"),
        "desc": gettext("# of people currently in ICU"),
        "longdesc": gettext(
            "Total count of people currently in ICU and positive to COVID-19"
        ),
        "fa": "fas fa-procedures"
    },
    "totale_ospedalizzati": {
        "title": gettext("Total Hospitalized"),
        "desc": gettext("# of people currently hospitalized"),
        "longdesc": gettext(
            "Total count of people currently hospitalized. "
            "It takes into account ICU"),
        "fa": "fas fa-hospital-user"
    },
    "isolamento_domiciliare": {
        "title": gettext("Self Isolation"),
        "desc": gettext("# of people currently in self isolation"),
        "longdesc": gettext(
            "People currently positive but who don't need hospitalization"
        ),
        "fa": "fas fa-house-user"
    },
    "totale_positivi": {
        "title": gettext("Total Positive"),
        "desc": gettext(
            "# of people currently "
            "hospitalized with symptoms + ICU + self isolation"
        ),
        "longdesc": gettext(
            "People currently positive. "
            "Unlike 'Total Cases' it does not take into account "
            "'healed' and 'deaths'. By the end of the outbreak "
            "this should tend to zero. In particular, it is: "
            "total positive = total cases - total healed - total deaths"
        ),
        "fa": "fas fa-viruses"
    },
    "variazione_totale_positivi": {
        "title": gettext("Total Positive Variation"),
        "desc": gettext(
            "Variation of # of people currently positive "
            "with respect to yesterday"
        ),
        "longdesc": gettext(
            "Variation of the number of people currently positive "
            "with respect to the previous day. It is negative when the number "
            "of daily healed and deaths is larger than 'New positive'"
        ),
        "fa": "fas fa-chart-area"
    },
    "nuovi_positivi": {
        "title": gettext("New Positive"),
        "desc": gettext("Daily count of new positve cases"),
        "longdesc": gettext("Daily count of new positve cases"),
        "fa": "fas fa-virus"
    },
    "dimessi_guariti": {
        "title": gettext("Total Healed"),
        "desc": gettext("Cumulative # of people healed"),
        "longdesc": gettext(
            "Total number of people healed since the beginning of the outbreak"
        ),
        "fa": "far fa-smile"
    },
    "deceduti": {
        "title": gettext("Total Deaths"),
        "desc": gettext("Total deaths count"),
        "longdesc": gettext(
            "Total deaths count since the beginning of the outbreak"
        ),
        "fa": "fas fa-cross"
    },
    "totale_casi": {
        "title": gettext("Total Cases"),
        "desc": gettext(
            "Total count of the positive tests since the"
            " beginning of the outbreak"
        ),
        "longdesc": gettext(
            "Total count of the positive tests since the"
            " beginning of the outbreak"
        ),
        "fa": "fas fa-viruses"
    },
    "tamponi": {
        "title": gettext("Total Swabs"),
        "desc": gettext("# of swabs performed"),
        "longdesc": gettext(
            "Total number of swabs performed since the beginning of the outbreak"
        ),
        "fa": "fas fa-vial"
    },
    "deceduti_giornalieri": {
        "title": gettext("Daily deaths"),
        "desc": gettext("Daily deaths count"),
        "longdesc": gettext("Daily deaths count"),
        "fa": "fas fa-cross"
    }
}
#  The order here matters as it will be reflected in the webpage
CARD_TYPES = [
    "nuovi_positivi", "ricoverati_con_sintomi", "terapia_intensiva",
    "deceduti_giornalieri", "totale_positivi", "totale_ospedalizzati",
    "variazione_totale_positivi", "totale_casi", "isolamento_domiciliare",
    "dimessi_guariti", "deceduti", "tamponi"
]
CUSTOM_CARD = ["deceduti_giornalieri"]
CARD_MAP = {
    "deceduti_giornalieri": "deceduti"
}
REGION_KEY = "denominazione_regione"
PROVINCE_KEY = "denominazione_provincia"
PCM_DATE_FMT = "%Y-%m-%dT%H:%M:%S"
CHART_DATE_FMT = "%d %b"
UPDATE_FMT = "%d/%m/%Y %H:%M"
WEBSITE_TITLE = gettext("COVID-19 Italy Monitor")
PCM_DATE_KEY = "data"
LOCKDOWN_DAY = dt.datetime(2020, 3, 9)
LANGUAGES = {
    "en": "English",
    "it_IT": "Italiano"
}
REGIONS = [
    'Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia-Romagna',
    'Friuli Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia',
    'Marche', 'Molise', 'P.A. Bolzano', 'P.A. Trento', 'Piemonte',
    'Puglia', 'Sardegna', 'Sicilia', 'Toscana', 'Umbria',
    "Valle d'Aosta", 'Veneto'
]
PROVINCES = [
    'Agrigento', 'Alessandria', 'Ancona', 'Aosta', 'Arezzo',
    'Ascoli Piceno', 'Asti', 'Avellino', 'Bari',
    'Barletta-Andria-Trani', 'Belluno', 'Benevento', 'Bergamo',
    'Biella', 'Bologna', 'Bolzano', 'Brescia', 'Brindisi', 'Cagliari',
    'Caltanissetta', 'Campobasso', 'Caserta', 'Catania', 'Catanzaro',
    'Chieti', 'Como', 'Cosenza', 'Cremona', 'Crotone', 'Cuneo',
    'Enna', 'Fermo', 'Ferrara', 'Firenze', 'Foggia', 'Forlì-Cesena',
    'Frosinone', 'Genova', 'Gorizia', 'Grosseto', 'Imperia',
    'Isernia', "L'Aquila", 'La Spezia', 'Latina', 'Lecce', 'Lecco',
    'Livorno', 'Lodi', 'Lucca', 'Macerata', 'Mantova',
    'Massa Carrara', 'Matera', 'Messina', 'Milano', 'Modena',
    'Monza e della Brianza', 'Napoli', 'Novara', 'Nuoro', 'Oristano',
    'Padova', 'Palermo', 'Parma', 'Pavia', 'Perugia',
    'Pesaro e Urbino', 'Pescara', 'Piacenza', 'Pisa', 'Pistoia',
    'Pordenone', 'Potenza', 'Prato', 'Ragusa', 'Ravenna',
    'Reggio di Calabria', "Reggio nell'Emilia", 'Rieti', 'Rimini',
    'Roma', 'Rovigo', 'Salerno', 'Sassari', 'Savona', 'Siena',
    'Siracusa', 'Sondrio', 'Sud Sardegna', 'Taranto', 'Teramo',
    'Terni', 'Torino', 'Trapani', 'Trento', 'Treviso', 'Trieste',
    'Udine', 'Varese', 'Venezia', 'Verbano-Cusio-Ossola', 'Vercelli',
    'Verona', 'Vibo Valentia', 'Vicenza', 'Viterbo'
]
