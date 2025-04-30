import camelot
import os


class Vote:
    def __init__(self, source, output, grouped_tables, continious_tables, tables):
        """
        creates a vote object
        each vote has a source file, output file, conflict pages, and tables
        this vote object processes all the tables in a pdf source file 
        and outputs all clean tables in a csv file
        the pages that do not have clean tables are stored in the conflicting tables variable
        """
        self.source = source
        self.output = output
        self.grouped_tables = grouped_tables # page numbers and table names of multi tables per page 
        self.continious_tables = continious_tables # page numbers and table names of continious tables
        self.tables = tables # default tables


class VoteFactory:

    def __init__(self):
        self.source_path = os.path.join(os.getcwd(), 'data', 'input')
        self.output_path = os.path.join(os.getcwd(), 'data', 'output')

    # TODO: Table A.3.6 unprocessed
    def create_vote_1(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_1.pdf'),
            output=os.path.join(self.output_path, 'vote_1'),
            grouped_tables=[
                {"page": 9, "table_names": ['Table A.3','Table A.3.1', 'Table A.3.2']},
                {"page": 10, "table_names": ['Table A.3.3', 'Table A.3.4', 'Table A.3.5']},
            ],
            continious_tables=[],
            tables=['Table A.3.6'] # page 11 in pdf
        )
        return vote

    # Done
    def create_vote_2(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_2.pdf'),
            output=os.path.join(self.output_path, 'vote_2'),
            grouped_tables=[
                {"page": 7, "table_names": ['Table A.3','Table A.3.1', 'Table A.3.2', 'Table A.3.3']},
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3', 'Table A.2.4'
            ]
        )
        return vote

    #done
    def create_vote_3(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_3.pdf'),
            output=os.path.join(self.output_path, 'vote_3'),
            grouped_tables=[
              {"page": 12, "table_names": ['Table A.4.4', 'Table A.5', 'Table A.5.1']},
              {"page": 13, "table_names": ['Table A.5.2', 'Table A.5.3', 'Table A.5.4']},  
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3', 'Table A.2.4', 'Table A.3', 'Table A.4', 
                'Table A.4.1', 'Table A.4.2', 'Table A.4.3'
            ]
        )
        return vote

    #done
    def create_vote_4(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_4.pdf'),
            output=os.path.join(self.output_path, 'vote_4'),
            grouped_tables=[
                {"page": 8, "table_names": ['Table A.4','Table A.4.1']},
                {"page": 9, "table_names": ['Table A.4.2', 'Table A.4.3',  'Table A.4.4']},
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3', 'Table A.2.4', 'Table A.3', 'Table A.4.5', 
                'Table A.5', 'Table A.5.1', 'Table A.5.2', 'Table A.5.3',
                'Table A.5.4'
            ]
        )
        return vote

    #done
    def create_vote_5(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_5.pdf'),
            output=os.path.join(self.output_path, 'vote_5'),
            grouped_tables=[
                {"page": 5, "table_names": ['Table A.2.3', 'Table A.2.4']},
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.5', 'Table A.2.6', 'Table A.2.7', 'Table A.3', 
                'Table A.3.1', 'Table A.3.2', 'Table A.3.3', 'Table A.3.4', 
                'Table A.3.5', 'Table A.3.6', 'Table A.3.7'
            ]
        )
        return vote

    #done
    def create_vote_6(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_6.pdf'),
            output=os.path.join(self.output_path, 'vote_6'),
            grouped_tables=[
                {"page": 12, "table_names": ['Table A.3', 'Table A.3.1', 'Table A.3.2', 'Table A.3.3']},
                {"page": 13, "table_names": ['Table A.4.3', 'Table A.4.4']}
            ],
            continious_tables=[
                {"start_page": 2, "table_name": ['Table A.2']},
            ],
            tables=[
                'Table A.1', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 
                'Table A.2.4', 'Table A.2.5', 'Table A.2.6', 'Table A.2.7', 
                'Table A.2.8', 'Table A.4', 'Table A.4.1', 'Table A.4.2', 
                'Table A.4.5', 'Table A.4.6', 'Table A.4.7', 'Table A.4.8'
            ]
        )
        return vote

    #done
    def create_vote_7(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_7.pdf'),
            output=os.path.join(self.output_path, 'vote_7'),
            grouped_tables=[
                {"page": 8, "table_names": ['Table A.3', 'Table A.3.1']},
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3', 'Table A.2.4', 'Table A.2.5', 'Table A.4', 
                'Table A.4.1', 'Table A.4.2', 'Table A.4.3', 'Table A.4.4', 
                'Table A.4.5'
            ]
        )
        return vote

    # TODO: Missing table A.3.6 pg 375
    def create_vote_8(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_8.pdf'),
            output=os.path.join(self.output_path, 'vote_8'),
            continious_tables=[],
            grouped_tables=[
                {"page": 6, "table_names": ['Table A.3', 'Table A.3.1', 'Table A.3.2']},
                {"page": 7, "table_names": ['Table A.3.3', 'Table A.3.4', 'Table A.3.5']},
                {"page": 9, "table_names": ['Table A.4.1', 'Table A.4.2']}
            ],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3', 'Table A.4', 'Table A.4.3'
            ]
        )
        return vote

    # TODO: Note that the pdf input is missing a page (432)
    # with tables A.5.5 and A.5.6
    def create_vote_9(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_9.pdf'),
            output=os.path.join(self.output_path, 'vote_9'),
            grouped_tables= [
                {"page": 11, "table_names": ['Table A.4', 'Table A.4.1']},
                {"page": 13, "table_names": ['Table A.5.1', 'Table A.5.2', 'Table A.5.3']}
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3', 'Table A.2.4', 'Table A.2.5', 'Table A.2.6', 
                'Table A.2.7', 'Table A.3', 'Table A.5', 'Table A.5.4', 
                'Table A.5.7'
            ]
        )
        return vote

    def create_vote_10(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_10.pdf'),
            output=os.path.join(self.output_path, 'vote_10'),
            grouped_tables=[
                {"page": 13, "table_names": ['Table A.3.3', 'Table A.3.4']},
            ],
            continious_tables=[
                {"start_page": 2, "table_name": ['Table A.2']},
                {"start_page": 6, "table_name": ['Table A.2.3']}
            ],
            tables=[
                'Table A.1', 'Table A.2.1', 'Table A.2.2', 'Table A.2.4', 
                'Table A.2.5', 'Table A.3', 'Table A.3.1', 'Table A.3.2', 
                'Table A.3.5', 'Table A.3.6', 'Table A.3.7', 'Table A.4', 
                'Table A.4.1', 'Table A.4.2', 'Table A.4.3', 'Table A.4.4', 
                'Table A.4.5'
            ]
        )
        return vote

    # DONE
    def create_vote_11(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_11.pdf'),
            output=os.path.join(self.output_path, 'vote_11'),
            grouped_tables=[
                {"page": 20, "table_names": ['Table A.4.1', 'Table A.4.2']},
                {"page": 21, "table_names": ['Table A.4.3', 'Table A.4.4']},
                {"page": 22, "table_names": ['Table A.4.5', 'Table A.4.6']},
                {"page": 23, "table_names": ['Table A.4.7', 'Table A.4.8']}
            ],
            continious_tables=[
                {"start_page": 2, "table_name": "Table A.2"},
                {"start_page": 4, "table_name": "Table A.2.1"},
                {"start_page": 6, "table_name": "Table A.2.2"},
                {"start_page": 8, "table_name": "Table A.2.3"},
                {"start_page": 10, "table_name": "Table A.2.4"},
                {"start_page": 12, "table_name": "Table A.2.5"},
                {"start_page": 15, "table_name": "Table A.2.7"}
            ],
            tables=[
                'Table A.1', 'Table A.2.6', 'Table A.2.8', 'Table A.3', 'Table A.4'
            ]
        )
        return vote

    # TODO: Find missing tables A.5.3 - A.5.5 (incl)
    # not in pdf
    def create_vote_12(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_12.pdf'),
            output=os.path.join(self.output_path, 'vote_12'),
            grouped_tables=[
                {"page": 14, "table_names": ['Table A.4', 'Table A.4.1']},
                {"page": 15, "table_names": ['Table A.4.2', 'Table A.4.3', 'Table A.4.4']},
                {"page": 18, "table_names": ['Table A.5.1', 'Table A.5.2']},
                {"page": 19, "table_names": ['Table A.5.6', 'Table A.5.7']}
            ],
            continious_tables=[
                {"start_page": 2, "table_name": "Table A.2"},
            ],
            tables=[
                'Table A.1', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 
                'Table A.2.4', 'Table A.2.5', 'Table A.2.6', 'Table A.2.7',
                'Table A.3.1', 'Table A.3.2', 'Table A.3.3', 'Table A.4.5',
                'Table A.5'
            ]
        )
        return vote

    # DONE
    def create_vote_13(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_13.pdf'),
            output=os.path.join(self.output_path, 'vote_13'),
            grouped_tables=[
                {"page": 14, "table_names": ['Table A.4.3', 'Table A.4.4']},
                {"page": 17, "table_names": ['Table A.5.1', 'Table A.5.2']},
            ],
            continious_tables=[
                {"start_page": 2, "table_name": "Table A.2"},
            ],
            tables=[
                'Table A.1', 'Table A.2.1', 'Table A.2.2', 'Table A.2.3', 
                'Table A.2.4', 'Table A.3.1', 'Table A.3.2', 'Table A.3.3', 
                'Table A.4', 'Table A.4.1', 'Table A.4.2', 'Table A.4.5', 
                'Table A.5', 'Table A.5.3', 'Table A.5.4'
            ]
        )
        return vote

    # TODO: Find missing tables A.3.6 pg. 778; A.4.1 pg 785
    def create_vote_14(self):
        vote = Vote(
            source=os.path.join(self.source_path, 'Vote_14.pdf'),
            output=os.path.join(self.output_path, 'vote_14'),
            grouped_tables=[
                {"page": 8, "table_names": ['Table A.3.1', 'Table A.3.2']},
                {"page": 12, "table_names": ['Table A.3.7', 'Table A.3.8']},
                {"page": 14, "table_names": ['Table A.3.10', 'Table A.3.11']}
            ],
            continious_tables=[],
            tables=[
                'Table A.1', 'Table A.2', 'Table A.2.1', 'Table A.2.2', 
                'Table A.2.3','Table A.2.4', 'Table A.3', 'Table A.3.3',
                'Table A.3.4', 'Table A.3.5','Table A.3.9', 'Table A.3.12',
                'Table A.3.13', 'Table A.4','Table A.4.2','Table A.4.3',
                'Table A.4.4'
            ]
        )
        return vote

    def create_all_votes(self):
        votes = []
        votes.append(self.create_vote_1())
        votes.append(self.create_vote_2())
        votes.append(self.create_vote_3())
        votes.append(self.create_vote_4())
        votes.append(self.create_vote_5())
        votes.append(self.create_vote_6())
        votes.append(self.create_vote_7())
        votes.append(self.create_vote_8())
        votes.append(self.create_vote_9())
        votes.append(self.create_vote_10())
        votes.append(self.create_vote_11())
        votes.append(self.create_vote_12())
        votes.append(self.create_vote_13())
        votes.append(self.create_vote_14())
        return votes

class VoteProcessor:

    def write_table_to_csv(self, source, output, page_num: int, table_name: str):
        page_num = str(page_num)
        tables = camelot.read_pdf(source, flavor='hybrid', pages=page_num)
        for table in tables:
            table.to_csv(f'{output}/{table_name}.csv')

    def process_vote_default(self, vote):
        page_num = 1
        for i in range(len(vote.tables)):
            for j in range(len(vote.grouped_tables)):
                if vote.grouped_tables[j]["page"] == page_num:
                    page_num += 1
            for k in range(len(vote.continious_tables)):
                if vote.continious_tables[k]["start_page"] == page_num:
                    page_num += 2
            self.write_table_to_csv(vote.source, vote.output, page_num, vote.tables[i])
            page_num += 1

    def process_specific_page_single_table(self, vote, page_num: int, table_name: str):
        self.write_table_to_csv(vote.source, vote.output, page_num, table_name)

    def process_all_default_votes(self, votes):
        for vote in votes:
            self.process_vote_default(vote)

def main():
    vote_factory = VoteFactory()
    vote_processor = VoteProcessor()
    

if __name__ == "__main__":
    main()
