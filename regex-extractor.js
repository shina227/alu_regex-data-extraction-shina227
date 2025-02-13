function extractData(pattern, text) {
    return text.match(pattern) || [];
}

// Sample Data
const sampleText = `
Emails: user@example.com, firstname.lastname@company.co.rw
URLs: https://www.example.com, http://subdomain.example.org/page
Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56, $50
`;

// Regex Patterns
const patterns = {
    Emails: /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g,
    URLs: /https?:\/\/(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\S*)?/g,
    PhoneNumbers: /\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g,
    Hashtags: /#[A-Za-z0-9_]+/g,
    Currency: /\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?/g
};

// Run Extraction
for (const [key, pattern] of Object.entries(patterns)) {
    console.log(`${key}:`, extractData(pattern, sampleText));
}
