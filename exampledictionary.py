def dictionary(a):
    a = input("look for a word : ").lower().strip().replace(" ","")
    dictionaries = {
       "hair":"Any of the cylindrical, keratinized, often pigmented filaments characteristically growing from the epidermis of a mammal" ,
       "eye":"An eye is a sensory organ that allows an organism to perceive visual information. It detects light and converts it into electro-chemical impulses in neurons (neurones). It is part of an organism's visual system.",
       "nose":"The human nose is the first organ of the respiratory system. It is also the principal organ in the olfactory system. The shape of the nose is determined by the nasal bones and the nasal cartilages, including the nasal septum, which separates the nostrils and divides the nasal cavity into two.",
       "lip":"The lips are a horizontal pair of soft appendages attached to the jaws and are the most visible part of the mouth of many animals, including humans.[1] Mammal lips are soft, movable and serve to facilitate the ingestion of food (e.g. suckling and gulping) and the articulation of sound and speech. Human lips are also a somatosensory organ, and can be an erogenous zone when used in kissing and other acts of intimacy."
     }
    print(dictionaries.get(a))
    
    if a not in dictionaries:
        print("word not in dictionaries")
    else:
        print(dictionaries.get(a))