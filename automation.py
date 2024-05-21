import csv

# to read the csv file with the column names

with open('column_names.csv', newline='') as csvfile:
    column_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    header = next(column_reader)  # to skip the headers

    # to create the new csv file for custom lineage

    with open('links.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Source', 'Target', 'Association'])  # new headers for the custom lineage csv file
        
        # IDs related to the source and target table

        # reference_table_src = '22795e65-f8fa-30f6-b3a4-f550006d0eff://us-east-2-sandbox-betaaccess-poc/metadata/A56_ACT.txt~com.infa.odin.models.file.flat.FlatFile\n'
        # reference_table_trg = '78497f78-7d48-3153-9d09-14b7ba469515://DV_BETANXT_EXCHANGE/DV_BETAACCESS_RAW_STAGE/ACT~com.infa.odin.models.relational.Table\n'
        
        # here, you will need to provide the reference IDs and the appropriate association type that aligns with your custom lineage

        for row in column_reader:
            reference_source_id = f'22795e65-f8fa-30f6-b3a4-f550006d0eff://us-east-2-sandbox-betaaccess-poc/metadata/A56_ACT.txt/{row[0]}~com.infa.odin.models.file.flat.FlatField\n'
            reference_target_id = f'78497f78-7d48-3153-9d09-14b7ba469515://DV_BETANXT_EXCHANGE/DV_BETAACCESS_RAW_STAGE/ACT{row[0]}~com.infa.odin.models.relational.Column\n'
            association_type = 'core.DirectionalDataFlow' # core.ResourceParentChild | core.DataSourceParentChild | core.DataSetToDataElementParentship | core.DataSetDataFlow | core.DirectionalDataFlow
            writer.writerow([reference_source_id, reference_target_id, association_type])