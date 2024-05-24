import csv

# to read the csv file with the column names
def reader_file(file_name):
    
    with open(file_name, newline='') as csvfile:
        column_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        header = next(column_reader)  # to skip the headers

        # to create the new csv file for custom lineage

        with open('links.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Source', 'Target', 'Association'])  # new headers for the custom lineage csv file
            
            # here, you will need to provide the reference IDs and the appropriate association type that aligns with your custom lineage

            for row in column_reader:
                reference_source_id = f'722228d3-d205-30cd-b708-1af37e1349c6://JDBC/A5/DCM_ACT/{row[0]}~com.infa.odin.models.relational.Column\n'
                reference_target_id = f'22795e65-f8fa-30f6-b3a4-f550006d0eff://us-east-2-sandbox-betaaccess-poc/metadata/A56_ACT.txt/{row[0]}~com.infa.odin.models.file.flat.FlatField\n'
                association_type = 'core.DirectionalDataFlow' # core.ResourceParentChild | core.DataSourceParentChild | core.DataSetToDataElementParentship | core.DataSetDataFlow | core.DirectionalDataFlow
                writer.writerow([reference_source_id, reference_target_id, association_type])

reader_file('column_names.csv')