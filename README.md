# Ladybug Travel Assistant

Ladybug is a Python-based travel assistant that helps you find the best driving, public transit, and walking routes between two locations. It uses the Google Maps API and OpenAI's GPT 3.5 model. Run main.py to get results.

# TO-DO:
- [x] configure AI
- [ ] create chat history function and possible users class (save chat history on SQL)
- [ ] frontend
- [ ] connecting frontend and backend

# Requires: 
- pip install requests openai
- Google Maps API key
- OpenAI API key

## Example Output

```plaintext
Hi! I'm a ladybug, your travel assistant. Enter your origin, destination, and preferred mode of travel.

Origin: Harlem

Destination: Koreatown

Fetching response...



The best driving route from Harlem to Koreatown in New York City is via NY-9A S. The route is approximately 7.5 miles and will take around 31 minutes depending on traffic.

For public transit, you can take the subway from Harlem to Koreatown. Take the A or C train from 125th St to 42nd St-Port Authority Bus Terminal, and then walk to Koreatown. The total journey will take approximately 25-30 minutes.

If you prefer walking, you can walk the entire way from Harlem to Koreatown. The walking distance is approximately 7.5 miles and will take around 2 hours. The route is relatively straightforward and will take you through various neighborhoods and landmarks in Manhattan.
```
# Note

Please note that the accuracy and reliability of the route suggestions provided by the Ladybug travel assistant depends on the data and algorithms used by the Google Maps API and OpenAI's GPT-3 model.
