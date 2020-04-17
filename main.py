import win10toast
toaster = win10toast.ToastNotifier()
toaster.show_toast('This is AI!', 'Success! This is working',
                   icon_path=None, duration=10, threaded=False)
# wait for threaded notification to finish
while toaster.notification_active():
    time.sleep(0.1)
