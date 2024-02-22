class Feedback:
    def __init__(self, customer_name, rating, comment):
        self.customer_name = customer_name
        self.rating = rating
        self.comment = comment

class ReviewSystem:
    def __init__(self):
        self.reviews = []

    def leave_review(self, feedback):
        self.reviews.append(feedback)
        print("Thank you for your feedback!")

    def view_reviews(self):
        print("Reviews:")
        for review in self.reviews:
            print(f"Customer: {review.customer_name}, Rating: {review.rating}, Comment: {review.comment}")

# Example usage:
review_system = ReviewSystem()

# Customer leaves a review
feedback = Feedback("John Doe", 4, "Great food and service!")
review_system.leave_review(feedback)

# View all reviews
review_system.view_reviews()
