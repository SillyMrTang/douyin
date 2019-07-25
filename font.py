mapCodeToFont = {
    '0xe602': 'num_',
    '0xe603': 'num_1',
    '0xe604': 'num_2',
    '0xe605': 'num_3',
    '0xe606': 'num_4',
    '0xe607': 'num_5',
    '0xe608': 'num_6',
    '0xe609': 'num_7',
    '0xe60a': 'num_8',
    '0xe60b': 'num_9',
    '0xe60c': 'num_4',
    '0xe60d': 'num_1',
    '0xe60e': 'num_',
    '0xe60f': 'num_5',
    '0xe610': 'num_3',
    '0xe611': 'num_2',
    '0xe612': 'num_6',
    '0xe613': 'num_8',
    '0xe614': 'num_9',
    '0xe615': 'num_7',
    '0xe616': 'num_1',
    '0xe617': 'num_3',
    '0xe618': 'num_',
    '0xe619': 'num_4',
    '0xe61a': 'num_2',
    '0xe61b': 'num_5',
    '0xe61c': 'num_8',
    '0xe61d': 'num_9',
    '0xe61e': 'num_7',
    '0xe61f': 'num_6',
}
mapFontToNum = {
    'num_': 1,
    'num_1': 0,
    'num_2': 3,
    'num_3': 2,
    'num_4': 4,
    'num_5': 5,
    'num_6': 6,
    'num_7': 9,
    'num_8': 7,
    'num_9': 8,
}


class GetDouyinNum(object):
    def __init__(self, code):
        self.code = code

    def get_num(self):
        dic = {}
        if self.code == '':
            return ''
        for i in self.code:
            j = i.replace(' &#', '0').replace('; ', '')
            dic[j] = str(mapFontToNum[mapCodeToFont[j]])
        return dic
