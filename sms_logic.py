import time

def send_fake_sms(number, count):
    output = []
    for i in range(count):
        output.append(f"Simulated sending SMS {i+1} to {number}")
        time.sleep(0.2)  # simulate delay
    return "\n".join(output)
  
