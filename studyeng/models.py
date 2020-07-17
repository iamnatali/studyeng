from django.db import models

class Category(models.Model):
    name = models.CharField('название категории', max_length=50)
    icon = models\
        .ImageField("иконка",upload_to='media/categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

class Level(models.Model):
    name = models.CharField('название уровня', max_length=50)
    code = models.CharField('код уровня', max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "уровень"
        verbose_name_plural = "уровни"

class Theme(models.Model):
    name = models.CharField('название темы', max_length=50)
    photo = models.ImageField('фото',upload_to='media/themes')
    category = models\
        .ForeignKey(Category, on_delete=models.CASCADE,
                    verbose_name='категория')
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              verbose_name='уровень')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тема"
        verbose_name_plural = "темы"

class Word(models.Model):
    name = models.CharField('слово', max_length=50)
    translation = models.CharField('перевод', max_length=50)
    transcription = models.CharField('транскрипция', max_length=50)
    example = models.TextField('пример', max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE,
                              verbose_name='тема')
    sound = models.FileField('звук', upload_to='media/sounds')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "слово"
        verbose_name_plural = "слова"