import camelot
import os


class Vote:
    def __init__(self, source, output, conflict_pages, tables):
        self.source = source
        self.output = output
        self.conflict_pages = conflict_pages
        self.table_names = tables


class VoteFactory:

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
    def __init__(self, pdf_path, output_parent_dir):
        self.pdf_path = pdf_path
        self.output_parent_dir = output_parent_dir


    def process_vote(self, vote):
        page_num = 1
        output_dir = os.path.join(self.output_parent_dir, )
        for i in range(len(vote.table_names)):
            if page_num not in vote.conflict_pages:
                self.write_table_to_csv(vote.source, vote.output, page_num, vote.table_names[i])
            page_num += 1

    def write_table_to_csv(self, filename: str, output, page_num: int, table_name: str):
        filename = os.path.join(self.pdf_path, filename)
        page_num = str(page_num)
        tables = camelot.read_pdf(filename, flavor='hybrid', pages=page_num)
        for table in tables:
            table.to_csv(f'{output}.csv')


def main():
    source = os.path.join(os.getcwd(), 'data', 'votes')
    output_parent_dir = os.path.join(os.getcwd(), 'data', 'output')
    vote_processor = VoteProcessor(source, output_parent_dir)
    vote_processor.process_vote_1()

if __name__ == "__main__":
    main()
