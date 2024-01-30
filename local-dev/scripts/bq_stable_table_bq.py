import argparse
from google.cloud import bigquery
from datetime import datetime

def copy_table(client, source_table_id, destination_table_id):
    """Copy original bq table from bq-demo-templates workspace to developer workspace."""
    job = client.copy_table(source_table_id, destination_table_id)
    job.result()
    print(f"The table {source_table_id} has been copied in {destination_table_id}.")

def update_table(client, table_id):
    """Update BQ table. This is an example."""
    # Here they (developers) should implement their update logic.
    # Ex: client.query("UPDATE QUERY HERE")
    pass

def main(project_id):
    client = bigquery.Client()

    source_table_id = "bq-demo-templates.carto-demo-data.demo_tilesets.osm_buildings"
    destination_table_id = f"{project_id}.carto-demo-data.demo_tilesets.osm_buildings"

    # Copy original table to developer workspace
    copy_table(client, source_table_id, destination_table_id)

    # Update develop table
    update_table(client, destination_table_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy and update BigQuery table")
    parser.add_argument("project_id", help="Please, input developer's project ID in GCP")
    args = parser.parse_args()

    main(args.project_id)
