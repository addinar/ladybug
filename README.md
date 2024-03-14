# Ladybug Travel Assistant

Ladybug is a Python-based travel assistant that helps you find the best driving, public transit, and walking routes between two locations. It uses the Google Maps API and OpenAI's GPT 3.5 model. Run main.py to get results.

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



The best driving route from Harlem, New York, NY to Koreatown, New York, NY is via FDR Dr, spanning about 7.6 miles and taking approximately 29 minutes.

For public transit, you can take the subway from Harlem to Koreatown. This route involves taking the 6 train from 125 St Station to Grand Central-42 St Station, then transferring to the Q train to 34 St-Herald Sq Station where you can walk to Koreatown.

If walking, the most direct route would be to head south on 7th Ave/Adam Clayton Powell Jr Blvd, turn left onto W 128th St, left onto Madison Ave, right onto E 132nd St, merge onto Harlem River Dr, continue onto FDR Dr, take exit 8 toward I-495/Midtown Tun/E 34 St, merge onto FDR Dr, turn right onto E 37th St, left onto 2nd Ave, right onto E 31st St, right onto 6th Ave/Ave of the Americas, and finally right onto W 32nd St to reach Koreatown.

If looking for an airline route from Harlem to Koreatown internationally, it would not be applicable as both are located within the city of New York..
```
# Note

Please note that the accuracy and reliability of the route suggestions provided by the Ladybug travel assistant depends on the data and algorithms used by the Google Maps API and OpenAI's GPT-3 model.
In addition, an ipynb file is attached if you wish to use that instead.
