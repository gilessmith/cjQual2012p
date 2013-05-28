
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


class GoogleDanceJam(CodeJamRunner):
    problem_name = 'B'
    problem_size = 'large-practice'
    
    def get_case_data(self, f):
        return [int(x) for x in f.readline().split(' ')]
        
    def execute_case(self, case_data):
        surprises = case_data[1]
        limit = case_data[2]
        limit_count = 0
        for googler in case_data[3:]:
            if (googler + 2) / 3 >= limit and googler >= limit:
                limit_count +=1
            elif surprises > 0 and (googler +4)/3 >=limit and googler >= limit:
                limit_count +=1
                surprises -= 1
        return limit_count

    def test(self):
       assert self.execute_case([3, 1, 5, 15, 13, 11]) == 3
       assert self.execute_case([3, 0, 8, 23, 22, 21]) == 2
       assert self.execute_case([2, 1, 1, 8, 0]) == 1
       assert self.execute_case([6, 2, 8, 29, 20, 8, 18, 18, 21]) == 3

       print 'tests passed'

if __name__ == '__main__':
    tdj = GoogleDanceJam()
    tdj.test()
    tdj.execute()

