from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from cve_app.models import CVE

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('CVE_1999_Data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cve_id = row['CVE ID']
                
                
                cve, created = CVE.objects.get_or_create(
                    cve_id=cve_id,
                    defaults={
                        'identifier': row['Identifier'],
                        'published_date': datetime.strptime(row['Published Date'], '%Y-%m-%d'),
                        'last_modified_date': datetime.strptime(row['Last Modified Date'], '%Y-%m-%d'),
                        'status': row['Status']
                    }
                )
                
                if created:
                    print(f"CVE ID {cve_id} created.")
                else:
                    print(f"CVE ID {cve_id} already exists.")