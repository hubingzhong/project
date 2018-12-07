from django.db import models
class Set(models.Model):
    setname = models.CharField('系统名称',max_length=64,null=True)
    setvalue = models.CharField('系统设置',max_length=200,null=True)
    class Meta:
        verbose_name = '系统设置'
        verbose_name_plural = '系统设置'
    def __str__(self):
        return self.setname

















