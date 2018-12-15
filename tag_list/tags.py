import boto3
Access_Key = 'AKIAJMAIXXXXXXXXXXXXXXXXXXXX'
Secret_key = 'TaMXD4AD+bVpjXXXXXXXXXXXXXXXXXXXXXX'

client = boto3.client('ec2','us-east-1',aws_access_key_id=Access_Key,aws_secret_access_key=Secret_key)

responce = client.describe_tags()

print "SR.NO,INSTANCE_Name,INSTANCE_ID,KEY,VALUE"
count = 1
### For Tags

def instance_id(x):
    for a in responce['Tags']:
        instance_id_a = a['ResourceType']
        instance_id_b = a['ResourceId']
        if instance_id_a == "instance":
            KEY = a['Key']
            VALUE = a['Value']
            if instance_id_b == x:
                print ",,," + KEY + "," + VALUE

#instance_id('i-02427eed33576f645')

### For Name
def instance_Name(x):
    for a in responce['Tags']:
        instance_id_a = a['ResourceType']
        instance_id_b = a['ResourceId']
        if instance_id_a == "instance":
            KEY = a['Key']
            VALUE = a['Value']
            if instance_id_b == x:
                if KEY == "Name":
                    return VALUE

instance_Name('i-02427eed33576f645')
#                print x
#instance_id('i-02427eed33576f645')


# List of instance id

l = []
for a in responce['Tags']:
    ints = a['ResourceType']
    ints_id = a['ResourceId']
    if ints == "instance":
        abc = a['ResourceId']
        key = a['Key']
        value = a['Value']
        l.append(abc)
#        print abc


list = set(l) 
for i in list:
#    print i
#    a = instance_Name(i)
    print count , "," , instance_Name(i) , "," , i  
    count = count + 1
    instance_id(i)
