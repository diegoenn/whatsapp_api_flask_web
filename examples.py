# mensaje simple
{"messaging_product": "whatsapp", 
 "preview_url": false, 
 "recipient_type": "individual", 
 "to": "+573015859341", 
 "type": "text", 
 "text": {"body": "Mensaje inicial al hacer clic en login!!!"}}

# mensaje usando template
{"messaging_product": "whatsapp", 
 "to": "+573015859341", 
 "type": "template", 
 "template": {
                "name": "sample_flight_confirmation", 
                "language": {"code": "en_US"}, 
                "components": [
                                {
                                    "type": "header", 
                                    "parameters": [
                                                    {
                                                        "type": "document", 
                                                        "document": {
                                                                        "filename": "FlightConfirmation.pdf", 
                                                                        "link": "https://drive.google.com/file/d/1bgUPlEU47dQ43PNApuFBGTj6h37F65gD/view?usp=sharing"
                                                                    }
                                                    }
                                                ]
                                },     
                                {
                                    "type": "body", 
                                    "parameters": [
                                                    {
                                                        "type": "text", 
                                                        "text": "Singapore (SIN)"
                                                    }, 
                                                    {
                                                        "type": "text", 
                                                        "text": "Denpasar (DPS)"
                                                    }, 
                                                    {
                                                        "type": "text", 
                                                        "text": "June 24, 2022 - 8:25 PM"
                                                    }
                                                ]
                                }
                            ]
            }
    }