# Generated by Django 4.2.6 on 2024-01-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0024_alter_funddistribution_financial_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funddistribution',
            name='financial_year',
            field=models.CharField(choices=[('2000-2001', '2000-2001'), ('2001-2002', '2001-2002'), ('2002-2003', '2002-2003'), ('2003-2004', '2003-2004'), ('2004-2005', '2004-2005'), ('2005-2006', '2005-2006'), ('2006-2007', '2006-2007'), ('2007-2008', '2007-2008'), ('2008-2009', '2008-2009'), ('2009-2010', '2009-2010'), ('2010-2011', '2010-2011'), ('2011-2012', '2011-2012'), ('2012-2013', '2012-2013'), ('2013-2014', '2013-2014'), ('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2018-2019', '2018-2019'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], max_length=9),
        ),
    ]
