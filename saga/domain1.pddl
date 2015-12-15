(define (domain domain1)
    (:requirements :strips :typing :equality)
    (:types
      Article Location Character - object
      Device - Article
    )
    (:predicates
        (IS_AT ?C1 - Character ?L1 - Location)
        (IS_TOOL ?D1 - Device)
        (HAS ?C1 - Character ?A1 - Article)
        (LOST ?A1 - Article)
        (BROKEN ?D1 - Device)
        (SAD ?C1 - Character)
        (HAPPY ?C1 - Character)
        (ANGRY ?C1 - Character)
        (EMBARASED ?C1 - Character)
        (POPULAR ?C1 - Character)
        (HUNGRY ?C1 - Character)
        (POOR ?C1 - Character)
        (RICH ?C1 - Character)
        (LOVE ?C1 - Character ?C2 - Character)
        (FLEX_MUSCLES ?C1 - Character)
        (MARRIED ?C1 - Character ?C2 - Character)
        (MARKETPLACE ?L1 - Location)
        (CLUMSY ?C1 - Character)
        (FOOD_VENDOR ?L1 - Location)
        (EDIBLE ?A1 - Article)
        (HERO ?C1 - Character)
        (FIRE ?L1 - Character)
        (LIGHTABLE ?A1 - Article)
        (LIT ?A1 - Article)
        (DESPERATE ?C1 - Character)
        (DIRTY ?C1 - Character)
        (HAS_FREE_STUFF ?L1 - Location)
        (HAS_WATER ?L1 - Location)
        (TEST ?C1 - Character)
        (NEW_HAIRCUT ?C1 - Character)
        (CUTS_HAIR ?L1 - Location)
        (HAS_GOOD_ADVICE ?C1 - Character)
        (HAS_JOB ?C1 - Character)
        (IS_HIRING ?L1 - Location)
    )
    (:action MOVE
        :parameters (
            ?C1 - Character
            ?L1 - Location
            ?L2 - Location
        )
        :precondition
            (IS_AT ?C1 ?L1)
        :effect (and
            (not (IS_AT ?C1 ?L1))
            (IS_AT ?C1 ?L2)
        )
    )
    (:action FIND
        :parameters (
            ?C1 - Character
            ?A1 - Article
            ?L1 - Location
        )
        :precondition (and
            (LOST ?A1)
            (IS_AT ?C1 ?L1)
            (IS_AT ?A1 ?L1)
        )
        :effect (and
            (HAS ?C1 ?A1)
            (not (LOST ?A1))
        )
    )
    (:action PUT_DOWN
        :parameters (
            ?C1 - Character
            ?A1 - Article
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (HAS ?C1 ?A1)
        )
        :effect (and
            (not (HAS ?C1 ?A1))
            (IS_AT ?A1 ?L1)
        )
    )
    (:action INSULT
        :parameters (
            ?C1 - Character
            ?C2 - Character
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (ANGRY ?C1)
        )
        :effect (and
            (not (HAPPY ?C2))
            (ANGRY ?C2)
        )
    )
    (:action COMPLEMENT
        :parameters (
            ?C1 - Character
            ?C2 - Character
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (HAPPY ?C1)
        )
        :effect (and
            (not (ANGRY ?C2))
            (not (SAD ?C2))
            (HAPPY ?C2)
        )
    )
    (:action LIKE
        :parameters (
            ?C1 - Character
            ?C2 - Character
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (HAPPY ?C1)
            (HAPPY ?C2)
        )
        :effect (and
            (POPULAR ?C2)
        )
    )
    (:action STEAL
        :parameters (
            ?C1 - Character
            ?L1 - Location
            ?D1 - Device
        )
        :precondition (and
            (MARKETPLACE ?L1)
            (IS_AT ?C1 ?L1)
            (IS_AT ?D1 ?L1)
            (not (HAS ?C1 ?D1))
        )
        :effect (and
            (not (IS_AT ?D1 ?L1))
            (HAS ?C1 ?D1)
        )
    )
    (:action FIX
        :parameters (
            ?C1 - Character
            ?D1 - Device
            ?D2 - Device
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (not (= ?D1 ?D2))
            (IS_TOOL ?D1)
            (HAS ?C1 ?D1)
            (IS_AT ?D2 ?L1)
            (BROKEN ?D2)
        )
        :effect (and
            (not (BROKEN ?D2))
            (FLEX_MUSCLES ?C1)
        )
    )
    (:action GET_IN_LOVE
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (FLEX_MUSCLES ?C2)
        )
        :effect (and
            (LOVE ?C1 ?C2)
            (not (FLEX_MUSCLES ?C2))
        )
    )
    (:action GET_MARRIED
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (LOVE ?C1 ?C2)
            (LOVE ?C2 ?C1)
        )
        :effect (and
            (MARRIED ?C1 ?C2)
            (MARRIED ?C2 ?C1)
        )
    )
    (:action ORDER_FOOD
        :parameters (
            ?C1 - Character
            ?L1 - Location
            ?A1 - Article
        )
        :precondition (and
            (RICH ?C1)
            (HUNGRY ?C1)
            (IS_AT ?C1 ?L1)
            (IS_AT ?A1 ?L1)
            (FOOD_VENDOR ?L1)
            (EDIBLE ?A1)
        )
        :effect (and
            (not (IS_AT ?A1 ?L1))
            (HAS ?C1 ?A1)
        )
    )
    (:action SPILL
        :parameters (
            ?C1 - Character
            ?A1 - Article
        )
        :precondition (and
            (HAS ?C1 ?A1)
            (CLUMSY ?C1)
            (EDIBLE ?A1)
        )
        :effect (and
            (EMBARASED ?C1)
        )
    )
    (:action LAUGH_AT
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (EMBARASED ?C2)
        )
        :effect (and
            (HAPPY ?C1)
            (ANGRY ?C2)
        )
    )
    (:action PUNCH
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (HAPPY ?C1)
            (ANGRY ?C2)
            (EMBARASED ?C2)
        )
        :effect (and
            (not (HAPPY ?C1))
            (not (ANGRY ?C2))
            (not (EMBARASED ?C2))
            (SAD ?C1)
            (SAD ?C2)
        )
    )
    (:action LIGHT_CANDLE
        :parameters (
            ?C1 - Character
            ?A1 - Article
        )
        :precondition (and
            (HAS ?C1 ?A1)
            (LIGHTABLE ?A1)
            (not (LIT ?A1))
        )
        :effect (and
            (LIT ?A1)
        )
    )
    (:action START_FIRE
        :parameters (
            ?C1 - Character
            ?A1 - Article
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (HAS ?C1 ?A1)
            (LIT ?A1)
            (CLUMSY ?C1)
        )
        :effect (and
            (FIRE ?L1)
        )
    )
    (:action SAVE_FROM_FIRE
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (CLUMSY ?C2)
            (FIRE ?L1)
        )
        :effect (and
            (not (IS_AT ?C1 ?L1))
            (not (IS_AT ?C2 ?L1))
            (HERO ?C1)
        )
    )
    (:action SEARCH_FOR_FOOD
        :parameters (
            ?C1 - Character
            ?L1 - Location
        )
        :precondition (and
            (HAS_FREE_STUFF ?L1)
            (IS_AT ?C1 ?L1)
            (POOR ?C1)
            (HUNGRY ?C1)
        )
        :effect (and
            (DESPERATE ?C1)
            (DIRTY ?C1)
        )
    )
    (:action CLEAN
        :parameters (
            ?C1 - Character
            ?L1 - Location
        )
        :precondition (and
            (HAS_WATER ?L1)
            (IS_AT ?C1 ?L1)
            (DIRTY ?C1)
        )
        :effect (and
            (not (DIRTY ?C1))
        )
    )
    (:action BEG_FOR_FOOD
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
            ?A1 - Article
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (HAS ?C2 ?A1)
            (EDIBLE ?A1)
            (DESPERATE ?C1)
            (not (DIRTY ?C1))
        )
        :effect (and
            (not (DESPERATE ?C1))
            (not (HAS ?C2 ?A1))
            (HAS ?C1 ?A1)
        )
    )
    (:action EAT
        :parameters (
            ?C1 - Character
            ?A1 - Article
        )
        :precondition (and
            (HUNGRY ?C1)
            (EDIBLE ?A1)
            (HAS ?C1 ?A1)
        )
        :effect (and
            (not (HUNGRY ?C1))
        )
    )
    (:action GET_HAIRCUT
        :parameters (
            ?C1 - Character
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (CUTS_HAIR ?L1)
            (not (NEW_HAIRCUT ?C1))
        )
        :effect (and
            (NEW_HAIRCUT ?C1)
        )
    )
    (:action GET_GOOD_ADVICE
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?L1 - Location
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
            (HAS_GOOD_ADVICE ?C2)
        )
        :effect (and
            (HAS_GOOD_ADVICE ?C1)
        )
    )
    (:action JOB_INTERVIEW
        :parameters (
            ?C1 - Character
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (NEW_HAIRCUT ?C1)
            (HAS_GOOD_ADVICE ?C1)
            (IS_HIRING ?L1)
        )
        :effect (and
            (HAS_JOB ?C1)
            (not (IS_HIRING ?L1))
        )
    )
)
