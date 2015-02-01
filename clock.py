from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
import worker
import requests


sched = BlockingScheduler()

def new_reminder(reminderDate):
	@sched.add_job(my_job, 'date', run_date=reminderDate, args=['text'])
#    @sched.interval_schedule(seconds=2)
	def job_function():
		queue = Queue(connection=conn)
		return()
#        print "Hello World"



sched.start()
