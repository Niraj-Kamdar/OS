from . import shell
from .scheduler import Scheduler

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.new(shell.main())
    scheduler.mainloop()