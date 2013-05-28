
class CodeJamRunner(object):

    def execute(self):
        with open('%s-%s.in' % (self.problem_name,self.problem_size)) as f:
            case_count = int(f.readline())
            case =0
            results = []
            while case<case_count:
                results.append(self.execute_case(self.get_case_data(f)))

                case += 1

        with open('%s-%s.out' %
                           (self.problem_name,
                            self.problem_size), 'w') as output:
             for i, result in enumerate(results):
                 output.write('Case #%s: %s\n' % (i+1, result))

mappings = {
'y':'a',
'n':'b',
'f':'c',
'i':'d',
'c':'e',
'w':'f',
'l':'g',
'b':'h',
'k':'i',
'u':'j',
'o':'k',
'm':'l',
'x':'m',
's':'n',
'e':'o',
'v':'p',
'z':'q',
'p':'r',
'd':'s',
'r':'t',
'j':'u',
'g':'v',
't':'w',
'h':'x',
'a':'y',
'q':'z',
' ':' '
}


class GooglereseJam(CodeJamRunner):
    problem_name = 'A'
    problem_size = 'small-practice'
    
    def get_case_data(self, f):
        return f.readline().strip()
        
    def execute_case(self, encoded):
        return ''.join([mappings[l] for l in encoded])

    def test(self):
        
        assert self.execute_case('ejp mysljylc kd kxveddknmc re jsicpdrysi') == 'our language is impossible to understand'
        assert self.execute_case('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd') == 'there are twenty six factorial possibilities'
        assert self.execute_case('de kr kd eoya kw aej tysr re ujdr lkgc jv') == 'so it is okay if you want to just give up'

if __name__ == '__main__':
    tdj = GooglereseJam()
    tdj.test()
    tdj.execute()

