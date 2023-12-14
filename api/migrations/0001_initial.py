# Generated by Django 5.0 on 2023-12-14 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('lecture_price', models.PositiveIntegerField()),
                ('package_size', models.PositiveSmallIntegerField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UsersRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.user')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(blank=True, max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('governorate', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('personal_photo', models.ImageField(upload_to='')),
                ('national_ID_photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.user')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(blank=True, max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('academic_year', models.CharField(choices=[(1, 'Junior 1'), (2, 'Junior 2'), (3, 'Junior 3'), (4, 'Junior 4'), (5, 'Junior 5'), (6, 'Junior 6'), (1, 'Middle 7'), (2, 'Middle 8'), (3, 'Middle 9'), (1, 'Senior 10'), (2, 'Senior 11'), (3, 'Senior 12')], max_length=10)),
                ('study_field', models.CharField(blank=True, choices=[(0, '3elmy 3loom'), (1, '3elmy reyada'), (2, 'Adaby')], max_length=15, null=True)),
                ('governorate', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('parent_phone_number', models.IntegerField()),
                ('parent_name', models.CharField(max_length=60)),
                ('points', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('verified', models.BooleanField(default=False)),
                ('personal_photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.user')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(blank=True, max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('governorate', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('balance', models.PositiveIntegerField()),
                ('accepted', models.BooleanField()),
                ('personal_photo', models.ImageField(upload_to='')),
                ('national_ID_photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_title', models.CharField(max_length=150)),
                ('video_path', models.CharField(max_length=250)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_path', models.CharField(max_length=250)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.subject'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usersrole'),
        ),
        migrations.CreateModel(
            name='Warnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBalanceTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='PointsTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='CourseRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='api.Enrollment', to='api.student'),
        ),
        migrations.CreateModel(
            name='BadgeEarning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.badge')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.AddField(
            model_name='badge',
            name='students',
            field=models.ManyToManyField(through='api.BadgeEarning', to='api.student'),
        ),
        migrations.CreateModel(
            name='AssistantRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.assistant')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='TeachRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('date_reviewed', models.DateTimeField()),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherBalanceTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(through='api.Teaching', to='api.teacher'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.teacher'),
        ),
        migrations.CreateModel(
            name='AssistanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('accepted', models.BooleanField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.assistant')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.AddConstraint(
            model_name='courserating',
            constraint=models.CheckConstraint(check=models.Q(('rating__lte', 5)), name='course_rate_lte_5'),
        ),
        migrations.AlterUniqueTogether(
            name='courserating',
            unique_together={('student', 'course')},
        ),
        migrations.AlterUniqueTogether(
            name='badgeearning',
            unique_together={('student', 'badge')},
        ),
        migrations.AddConstraint(
            model_name='assistantrating',
            constraint=models.CheckConstraint(check=models.Q(('rating__lte', 5)), name='assistant_rate_lte_5'),
        ),
        migrations.AlterUniqueTogether(
            name='assistantrating',
            unique_together={('student', 'assistant')},
        ),
        migrations.AlterUniqueTogether(
            name='teaching',
            unique_together={('subject', 'teacher')},
        ),
        migrations.AddConstraint(
            model_name='teacherrating',
            constraint=models.CheckConstraint(check=models.Q(('rating__lte', 5)), name='teacher_rate_lte_5'),
        ),
        migrations.AlterUniqueTogether(
            name='teacherrating',
            unique_together={('student', 'teacher')},
        ),
    ]
