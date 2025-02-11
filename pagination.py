import boto3

cloudtrail = boto3.client('cloudtrail')

start_time = '2022-07-25T00:00:00Z'
end_time = '2022-07-26T00:00:00Z'
max_results = 1000

response = cloudtrail.lookup_events(
    StartTime=start_time,
    EndTime=end_time,
    MaxResults=max_results
)

events = response['Events']
next_token = response.get('NextToken')

while next_token:
    response = cloudtrail.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        MaxResults=max_results,
        NextToken=next_token
    )

    events.extend(response['Events'])
    next_token = response.get('NextToken')
