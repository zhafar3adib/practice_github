import csv
import json

# Base Extractor class
class Extractor:
    def extract(self):
        raise NotImplementedError("Subclasses must implement this method")

# CSV Extractor
class CSVExtractor(Extractor):
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        # Implement CSV extraction logic here
        data = []
        with open(self.file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

# JSON Extractor
class JSONExtractor(Extractor):
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        # Implement JSON extraction logic here
        with open(self.file_path, mode='r') as f:
            data = json.load(f)
        return data

# Transformer
class Transformer:
    def transform(self, data):
        # Implement transformation logic here
        transformed_data = []
        for record in data:
            record_dict = dict()
            for k, v in record.items():
                if isinstance(v, str):
                    record_dict[k] = v.strip().upper()
            record_dict.update({"processed": True})
            transformed_data.append(record_dict)
        return transformed_data

# Loader
class Loader:
    def __init__(self):
        self.data = []

    def load(self, data):
        # Implement loading logic here
        self.data.extend(data)

# ETL Pipeline
class ETLPipeline:
    def __init__(self, extractors, transformer, loader):
        self.extractors = extractors
        self.transformer = transformer
        self.loader = loader

    def run(self):
        # Implement the ETL process here
        extracted_data = []
        for extractor in self.extractors:
            extracted_data.extend(extractor.extract())

        transformed_data = self.transformer.transform(extracted_data)
        self.loader.load(transformed_data)

# Test the pipeline
if __name__ == "__main__":
    # Define extractors
    csv_extractor = CSVExtractor(file_path="Session7_data.csv")
    json_extractor = JSONExtractor(file_path="Session7_data.json")

    # Define transformer and loader
    transformer = Transformer()
    loader = Loader()

    # Create and run the pipeline
    etl_pipeline = ETLPipeline(
        extractors=[csv_extractor, json_extractor], 
        transformer=transformer, 
        loader=loader
    )
    etl_pipeline.run()

    # Print the loaded data
    print(loader.data)