# Define a function for owner response
def owner_response(user_input):
    if "hello" in user_input.lower():
        return "Hello, how can I assist you?"
    elif "Discount for first customer" in user_input.lower():
        return "Yes, we do! If you're a first-time customer, you can get 10% off your first service. Just mentioned the code 'NEW10' when you come in for your appointment"

    elif "Service" in user_input.lower():
        return "We offer: haircuts\n- beard trims\n- Shaves\n- Variety og grooming services\n- body massage\n- Spa"
    elif "thanks" in user_input.lower() or "thank you" in user_input.lower():
        return "You're welcome! Have a great day."
    elif "booking an appointment" in user_input.lower():
         return "Hello,thank you for reaching out! Yes, we have availability this week. "
    elif "Prices for haircut" in user_input.lower():
         return "We provide all types of haircuts in just RS.299/-"
    elif "Price for Facial massage" in user_input.lower():
         return "We provide full Facial massage in just RS.199/-"
        
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"

# Main conversation loop
while True:
    # Get user input
    user_input = input("Client: ")

    # Check for exit command
    if user_input.lower() == "exit":
        print("Owner: Goodbye!")
        break

    # Owner response
    owner_resp = owner_response(user_input)

    # Print owner response
    print("Owner: " + owner_resp)
