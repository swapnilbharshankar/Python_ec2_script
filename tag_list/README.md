# List the instance name, Instance ID, Tags

To get the output in python

```
python tags.py > output.csv

```

```
SR.NO	INSTANCE_Name	INSTANCE_ID	KEY	VALUE
1	 WordPress-Demo 	 i-08a777645d2bd811b		
			Name	WordPress-Demo
			aws:cloudformation:logical-id	WebServer
			aws:cloudformation:stack-id	arn:aws:cloudformation:us-east-1:884007744260:stack/WP-MYSQL-Single-Instance/3fb23950-d853-11e8-940a-500c28688861
			aws:cloudformation:stack-name	WP-MYSQL-Single-Instance
2	 SDApp1 	 i-08cce8bbc45455934		
			Name	SDApp1
3	 Jenkins-new 	 i-0ea4e4a070196dd3f		
			Name	Jenkins-new
4	 Ansible 	 i-02427eed33576f645		
			Backup	TRUE
			Name	Ansible

```
