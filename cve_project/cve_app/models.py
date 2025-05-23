from django.db import models

class CVE(models.Model):
    cve_id = models.CharField(max_length=20, unique=True)
    identifier = models.CharField(max_length=20)
    published_date = models.DateField()
    last_modified_date = models.DateField()
    status = models.CharField(max_length=20, choices = [
        ('ANALYZED', 'Analyzed'),
        ('MODIFIED', 'Modified'),
        ('REJECTED', 'Rejected')
    ])
    class Meta:
        ordering = ['-last_modified_date'] 
        

    def _str_(self):
        return self.cve_id

