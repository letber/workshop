from datetime import datetime


class TodoInterface:
    def __init__(self, filename):
        self.filename = filename
        self.deadlines = self.get_all_deadlines()

    def get_all_deadlines(self):
        """ Get all deadlines from file """
        # TODO: get all deadlines from file
        return None

    @property
    def today(self):
        return datetime.now()

    def get_deadlines_list(self, day):
        """ Getting deadlines at day and returning them as list """
        # Todo: Getting deadlines at day and returning them as list

        return []

    def print_deadlines(self, day):
        print(f"Deadlines for {day}: ")
        for line in self.get_deadlines_list(day):
            print(line)


    def command_handler(self):
        line = input()

        if line.startswith('stop_program'):
            return False

        if line.startswith('create'):
            # Todo: Create new task
            # Includes: parsing, getting todo_date in datetime.date format
            todo_date = None

            self.print_deadlines(todo_date)
            if len(self.get_deadlines_list(todo_date)) == 1:
                print('Priority was set as 1')
                priority = 1
            else:
                print('Please print priority: ')
                priority = int(input('Priority: '))

            # TODO: save task

        elif line.startswith('Find all deadlines by date: '):
            todo_list_date = datetime.strptime(line.split(':')[1], '%d.%m.%y')
            self.print_deadlines(todo_list_date)

        return True

    def main(self):
        run = True
        while run:
            self.get_all_deadlines()
            self.print_deadlines(self.today)
            run = self.command_handler()


if __name__ == '__main__':
    TodoInterface('filename.csv').main()
