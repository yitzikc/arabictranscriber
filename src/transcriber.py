
'''
Created on 17 Sep 2016

@author: yc
'''


class Ar2He(object):
    '''
    Arabic -> Hebrew transcriber
    '''

    __Ar2HeNormalizedTranslitTbl = {
        "\N{ARABIC LETTER HAMZA}": "\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER ALEF WITH MADDA ABOVE}": "\N{HEBREW LETTER ALEF}\N{HEBREW POINT PATAH}\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER ALEF WITH HAMZA ABOVE}": "\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER WAW WITH HAMZA ABOVE}":  "\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER ALEF WITH HAMZA BELOW}": "\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER YEH WITH HAMZA ABOVE}":  "\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER ALEF}": "\N{HEBREW LETTER ALEF}",
        "\N{ARABIC LETTER BEH}":  "\N{HEBREW LETTER BET}\N{HEBREW POINT DAGESH OR MAPIQ}",
        "\N{ARABIC LETTER PEH}":  "\N{HEBREW LETTER PE}\N{HEBREW POINT DAGESH OR MAPIQ}",
        "\N{ARABIC LETTER TEH MARBUTA}": "\N{HEBREW LETTER HE}",
        "\N{ARABIC LETTER TEH}":   "\N{HEBREW LETTER TAV}",
        "\N{ARABIC LETTER THEH}":  "\N{HEBREW LETTER TAV}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER JEEM}":  "\N{HEBREW LETTER ZAYIN}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER HAH}":   "\N{HEBREW LETTER HET}",
        "\N{ARABIC LETTER KHAH}":  "\N{HEBREW LETTER HET}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER DAL}":   "\N{HEBREW LETTER DALET}",
        "\N{ARABIC LETTER THAL}":  "\N{HEBREW LETTER DALET}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER REH}":   "\N{HEBREW LETTER RESH}",
        "\N{ARABIC LETTER ZAIN}":  "\N{HEBREW LETTER ZAYIN}",
        "\N{ARABIC LETTER SEEN}":  "\N{HEBREW LETTER SAMEKH}",
        "\N{ARABIC LETTER SHEEN}": "\N{HEBREW LETTER SHIN}\N{HEBREW POINT SHIN DOT}",
        "\N{ARABIC LETTER SAD}":   "\N{HEBREW LETTER TSADI}",
        "\N{ARABIC LETTER DAD}":   "\N{HEBREW LETTER TSADI}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER TAH}":   "\N{HEBREW LETTER TET}",
        "\N{ARABIC LETTER ZAH}":   "\N{HEBREW LETTER TET}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER AIN}":   "\N{HEBREW LETTER AYIN}",
        "\N{ARABIC LETTER GHAIN}": "\N{HEBREW LETTER AYIN}\N{HEBREW PUNCTUATION GERESH}",
        "\N{ARABIC LETTER FEH}":   "\N{HEBREW LETTER PE}",
        "\N{ARABIC LETTER VEH}":   "\N{HEBREW LETTER BET}\N{HEBREW POINT RAFE}",
        "\N{ARABIC LETTER QAF}":   "\N{HEBREW LETTER QOF}",
        "\N{ARABIC LETTER KAF}":   "\N{HEBREW LETTER KAF}\N{HEBREW POINT DAGESH OR MAPIQ}",
        "\N{ARABIC LETTER GAF}":   "\N{HEBREW LETTER GIMEL}",
        "\N{ARABIC LETTER LAM}":   "\N{HEBREW LETTER LAMED}",
        "\N{ARABIC LETTER MEEM}":  "\N{HEBREW LETTER MEM}",
        "\N{ARABIC LETTER NOON}":  "\N{HEBREW LETTER NUN}",
        "\N{ARABIC LETTER HEH}":   "\N{HEBREW LETTER HE}",
        "\N{ARABIC LETTER WAW}":   "\N{HEBREW LETTER VAV}",
        "\N{ARABIC LETTER ALEF MAKSURA}":  "\N{HEBREW LETTER HE}",
        "\N{ARABIC LETTER YEH}":   "\N{HEBREW LETTER YOD}",
        
        # Tashkil - vowelization marks
        "\N{ARABIC FATHA}":  "\N{HEBREW POINT PATAH}",
        "\N{ARABIC DAMMA}":  "\N{HEBREW POINT QUBUTS}",
        "\N{ARABIC KASRA}":  "\N{HEBREW POINT HIRIQ}",
        "\N{ARABIC SHADDA}": "\N{HEBREW POINT DAGESH OR MAPIQ}",
        "\N{ARABIC SUKUN}":  "\N{HEBREW POINT SHEVA}",
                           }

    "A canonical representation of the sounds available in Arabic, including those that only exist in dialects and in loan-words"

    def Trasnslit2He(self, text):
        translitGen = ( c if c.isspace() else self.__Ar2HeNormalizedTranslitTbl.get(c, "") for c in text )
        return "".join(translitGen)


    # TODO: Add output-side filters in the Hebrew text, e.g. convert Mem, Nun etc. to their final form.


# Unit Tests


import unittest


class TestTranslit(unittest.TestCase):
    def setUp(self):
        self.ar2he = Ar2He()
        
    def checkMapping(self, expected):
        for ar, transcribed in expected.items():
            self.assertEqual(transcribed, self.ar2he.Trasnslit2He(ar))
    
    def test_simpleWords(self):
        expected = {
            "كتب": "כּתבּ",
            "رمى": "רמה",
            "لحظة": "לחט׳ה",
            "آخر": "אַאח׳ר",
            "فولكسڤاگن": "פולכּסבֿאגנ",
            "پاب": "פּאבּ",
                    }

        self.checkMapping(expected)
        
    def test_tashkil(self):
        expected = {
            "كَتَب": "כַּתַבּ",
            "كَتَّب": "כַּתַּבּ",
            "شُغْل": "שֻׁע׳ְל",
            "عِيد": "עִיד",
        }
        
        self.checkMapping(expected)



