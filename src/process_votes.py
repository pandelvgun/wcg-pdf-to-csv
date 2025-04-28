import camelot
import os


class Vote:
    def __init__(self, source, output, conflict_pages, tables):
        self.source = source
        self.output = output
        self.conflict_pages = conflict_pages
        self.table_names = tables


class VoteFactory:

    def __init__(self):
        self.source_path = os.path.join(os.getcwd(), 'data', 'input')
        self.output_path = os.path.join(os.getcwd(), 'data', 'output')

    def create_vote_1():
        pass

    def create_vote_2():
        pass

    def create_vote_3():
        pass

    def create_vote_4():
        pass

    def create_vote_5():
        pass

    def create_vote_6():
        pass

    def create_vote_7():
        pass

    def create_vote_8():
        pass

    def create_vote_9():
        pass

    def create_vote_10():
        pass

    def create_vote_11():
        pass

    def create_vote_12():
        pass

    def create_vote_13():
        pass

    def create_vote_14():
        pass


class VoteProcessor:
    def process_vote(self, vote):
        page_num = 1
        for i in range(len(vote.table_names)):
            if page_num not in vote.conflict_pages:
                self.write_table_to_csv(vote.source, vote.output, page_num, vote.table_names[i])
            page_num += 1

    def write_table_to_csv(self, source, output, page_num: int, table_name: str):
        page_num = str(page_num)
        tables = camelot.read_pdf(source, flavor='hybrid', pages=page_num)
        for table in tables:
            table.to_csv(f'{output}.csv')


def main():
    pass

if __name__ == "__main__":
    main()
