import camelot
import os


class Vote:
    def __init__(self, source, output, multi_table_pages, run_on_pages, tables):
        """
        creates a vote object
        each vote has a source file, output file, conflict pages, and tables
        this vote object processes all the tables in a pdf source file 
        and outputs all clean tables in a csv file
        the pages that do not have clean tables are stored in the conflicting tables variable
        """
        self.source = source
        self.output = output
        self.multi_table_pages = multi_table_pages
        self.run_on_pages = run_on_pages
        self.tables = tables 


class VoteFactory:

    def __init__(self):
        self.source_path = os.path.join(os.getcwd(), 'data', 'input')
        self.output_path = os.path.join(os.getcwd(), 'data', 'output')

    # TODO: add processing logic - did it already in testing of concept
    # However some tables did not get processed. Need to fix
    def create_vote_1():
        pass

    def create_vote_2(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_2.pdf'),
            output=os.path.join(self.output_path, 'vote_2'),
            multi_table_pages=[7],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.2.4']
        )
        return vote

    def create_vote_3(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_3.pdf'),
            output=os.path.join(self.output_path, 'vote_3'),
            multi_table_pages=[12, 13],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.2.4', 'Table A.3', 'Table A.4', 'Table A.4.1', 'Table A.4.2', 'Table A.4.3']
        )
        return vote

    def create_vote_4(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_4.pdf'),
            output=os.path.join(self.output_path, 'vote_4'),
            multi_table_pages=[8, 9],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.2.4', 'Table A.3', 'Table A.4.5', 'Table A.5', 'Table A.5.1', 'Table A.5.2', 'Table A.5.3', 'Table A.5.4']
        )
        return vote

    def create_vote_5(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_5.pdf'),
            output=os.path.join(self.output_path, 'vote_5'),
            multi_table_pages=[5],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.5', 'Table A.2.6', 'Table A.2.7', 'Table A.3', 'Table A.3.1', 'Table A.3.2', 'Table A.3.3', 'Table A.3.4', 'Table A.3.5', 'Table A.3.6', 'Table A.3.7']
        )
        return vote

    def create_vote_6(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_6.pdf'),
            output=os.path.join(self.output_path, 'vote_6'),
            multi_table_pages=[2, 3, 12, 16],
            tables=['Table A.1', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.2.4', 'Table A.2.5', 'Table A.2.6', 'Table A.2.7', 'Table A.2.8', 'Table A.4', 'Table A.4.1', 'Table A.4.2', 'Table A.4.5', 'Table A.4.6', 'Table A.4.7', 'Table A.4.8']
        )
        return vote

    def create_vote_7(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_7.pdf'),
            output=os.path.join(self.output_path, 'vote_7'),
            multi_table_pages=[8],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.2.4', 'Table A.2.5', 'Table A.4', 'Table A.4.1', 'Table A.4.2', 'Table A.4.3', 'Table A.4.4', 'Table A.4.5']
        )
        return vote

    def create_vote_8(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_8.pdf'),
            output=os.path.join(self.output_path, 'vote_8'),
            multi_table_pages=[6,7,9],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.4', 'Table A.4.3']
        )
        return vote

    # TODO: Note that the pdf input is missing a page (432)
    # with tables A.5.5 and A.5.6
    # this should be fixed 
    def create_vote_9(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_9.pdf'),
            output=os.path.join(self.output_path, 'vote_9'),
            multi_table_pages=[11, 13],
            tables=['Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 'Table A.2.4', 'Table A.2.5', 'Table A.2.6', 'Table A.2.7', 'Table A.3', 'Table A.5', 'Table A.5.4', 'Table A.5.7']
        )
        return vote

    def create_vote_10(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_10.pdf'),
            output=os.path.join(self.output_path, 'vote_10'),
            multi_table_pages=[2, 3, 6, 7, 13],
            tables=['Table A.1', 'Table A.2.1', 'Table A.2.2', 'Table A.2.4', 'Table A.2.5', 'Table A.3', 'Table A.3.1', 'Table A.3.2', 'Table A.3.5', 'Table A.3.6', 'Table A.3.7', 'Table A.4', 'Table A.4.1', 'Table A.4.2', 'Table A.4.3', 'Table A.4.4', 'Table A.4.5']
        )
        return vote

    # NOTE: This vote has a lot of tables that take 2 pages for a single table
    # need to investigate this case by itself
    # for now conflict pages stores pages with 
    # 1. multiple tables per page
    # 2. tables that take 2 pages
    def create_vote_11(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_11.pdf'),
            output=os.path.join(self.output_path, 'vote_11'),
            run_on_pages=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16],
            tables=['Table A.1', 'Table A.2.6', 'Table A.2.8', 'Table A.3', 'Table A.4']
        )
        return vote

    def create_vote_12(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_12.pdf'),
            output=os.path.join(self.output_path, 'vote_12'),
            multi_table_pages=[],
            tables=['']
        )
        return vote

    def create_vote_13(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_13.pdf'),
            output=os.path.join(self.output_path, 'vote_13'),
            multi_table_pages=[],
            tables=[]
        )
        return vote

    def create_vote_14(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_14.pdf'),
            output=os.path.join(self.output_path, 'vote_14'),
            multi_table_pages=[],
            tables=[]
        )
        return vote


class VoteProcessor:
    def process_vote_default(self, vote):
        page_num = 1
        for i in range(len(vote.table_names)):
            if page_num not in vote.multi_table_pages:
                self.write_table_to_csv(vote.source, vote.output, page_num, vote.tables[i])
            page_num += 1

    def write_table_to_csv(self, source, output, page_num: int, table_name: str):
        page_num = str(page_num)
        tables = camelot.read_pdf(source, flavor='hybrid', pages=page_num)
        for table in tables:
            table.to_csv(f'{output}/{table_name}.csv')


def main():
    pass

if __name__ == "__main__":
    main()
