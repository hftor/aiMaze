(define (domain domain1)
    (:requirements :strips :typing :equality)
    (:types
      Article Location Character - object
      Device - Article
    )
    (:predicates
        (IS_AT ?C1 - Character ?L1 - Location)
        (HAS ?C1 - Character ?A1 - Article)
        (LOST ?A1 - Article)
        (EDIBLE ?A1 - Article)
        (HUNGRY ?C1 - Character)
        (SAD ?C1 - Character)
        (HAPPY ?C1 - Character)
        (ANGRY ?C1 - Character)
        (POPULAR ?C1 - Character)
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
    (:action GIVE
        :parameters (
            ?C1 - Character
            ?C2 - Character
            ?A1 - Article
            ?L1 - Location
        )
        :precondition (and
            (not (= ?C1 ?C2))
            (HAS ?C1 ?A1)
            (IS_AT ?C1 ?L1)
            (IS_AT ?C2 ?L1)
        )
        :effect (and
            (not (HAS ?C1 ?A1))
            (HAS ?C2 ?A1)
        )
    )
    (:action LOSE
        :parameters (
            ?C1 - Character
            ?A1 - Article
            ?L1 - Location
        )
        :precondition (and
            (HAS ?C1 ?A1)
            (IS_AT ?C1 ?L1)
        )
        :effect (and
            (not (HAS ?C1 ?A1))
            (LOST ?A1)
            (IS_AT ?A1 ?L1)
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
    (:action EAT
        :parameters (
            ?C1 - Character
            ?A1 - Article
        )
        :precondition (and
            (HAS ?C1 ?A1)
            (EDIBLE ?A1)
        )
        :effect (and
            (not (HAS ?C1 ?A1))
            (not (EDIBLE ?A1))
            (not (HUNGRY ?C1))
        )
    )
    (:action PICK_UP
        :parameters (
            ?C1 - Character
            ?A1 - Article
            ?L1 - Location
        )
        :precondition (and
            (IS_AT ?C1 ?L1)
            (IS_AT ?A1 ?L1)
        )
        :effect (and
            (not (IS_AT ?A1 ?L1))
            (HAS ?C1 ?A1)
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
)
