from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=255, null=True, default="", unique=True)
    code = models.CharField(max_length=10, null=True, default="", unique=True)
    image = models.ImageField(default='default.png', upload_to='sport_pics')

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'

    def __str__(self):
        return self.name


class Court(models.Model):
    name = models.CharField(max_length=255, null=True, default="")  #indoor/outdoor/courttype
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Court'
        verbose_name_plural = 'Courts'

    def __str__(self):
        return self.sport.name + " " + self.name


class Inventory(models.Model):
    name = models.CharField(max_length=255, null=True, default="", unique=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return self.sport.name + ":" + self.name


class Slot(models.Model):       #currently manual, but can be automated too
    date = models.DateField(null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'

    def __str__(self):
        return self.sport.name + " " + str(self.date)
