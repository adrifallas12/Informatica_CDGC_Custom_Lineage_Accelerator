# Informatica CDGC Custom Lineage Accelerator

# Overview
Informatica is a data processing platform that helps companies process and manage large amounts of data by integrating, cleansing, and managing data from various sources. It allows businesses to combine data from different sources, such as customer records, sales figures, and market trends, to gain valuable insights and make informed decisions. By transforming raw data into meaningful information, Informatica ensures the quality and consistency of data, enabling accurate, reliable, and up-to-date information.

In Cloud Data Governance and Catalog (CDGC), you cannot use the custom catalog source to establish the lineage between the Datasets. Instead, you have to use the bulk import option to populate the lineage across the Datasets.

**In this repository, you will find a script to automate the creation of the links.csv file necessary for establishing a [Custom Lineage](https://www.youtube.com/watch?v=wZM0ksDHPDE).**

## Prerequisites
Before you begin, ensure you have met the following requirements:

* Have installed a code editor (e.g. VS Code]
* A csv file with the name of the columns
* Supply one reference ID from your source and target tables in Informatica CDGC

## Usage
To effectively use this project, follow the instructions below:

+ **Reference IDs:** Insert the appropriate reference IDs in the designated fields as required
+ **Association Type:** Complete the '_association_type_' field with the association type that corresponds to data your lineage

Detailed Steps:

Insert Reference IDs:

- Identify and gather all necessary reference IDs (from source and target tables).
- Navigate to the section or field in the application where reference IDs are required.
- Enter the reference IDs accurately to ensure proper linkage and data integrity.

Fill in Association Type:

- Determine the correct association type for your data lineage.
- Locate the '_association_type_' field within the application.
- Input the determined association type to ensure correct data mapping and relationship tracking.

By following these steps, you will ensure that your data is accurately referenced and associated, maintaining the integrity and reliability of your information.


> [!TIP]
> Here you have a additional documentation about how to create a [Custom Lineage](https://docs.google.com/document/d/1B3cFHv8dGwic-ZP4b8yjbZw12qf-1cPoKfP4-dea1sY/edit?usp=sharing) in Informatica.



