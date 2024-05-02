Feature: Apply Job at Applied Materials

Scenario: Validate toast message while applying for job

When I launch 'https://www.appliedmaterials.com/'
Then I validate title as 'India English - Home'
And I click and navigate to 'Careers' on same tab
Then I validate title as 'Careers'
Then I click and navigate to 'Search Jobs' on new tab
And I expect 'What Will You Make Possible?' to be visible
Then I validate title as 'Careers at Applied Materials'
Then I click on select file and upload 'aMaterials.txt' and verify file is uploaded
And I search for 'Automation' and select 'Test Automation' from dropdown
And I click on job title 'position-card-1' and verify job Id contains 'ID: R'
And I apply for job and verify the toast message
Then I capture screenshot of current page
