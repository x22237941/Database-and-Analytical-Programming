from dagster import solid, pipeline, repository

@solid
def my_solid(context):
    return "Dagster in use!"

@pipeline
def my_pipeline():
    return my_solid()

# Define a repository containing our pipeline
@repository
def my_repository():
    return [my_pipeline]
